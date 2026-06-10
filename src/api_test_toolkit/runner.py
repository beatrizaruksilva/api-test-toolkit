import httpx
from api_test_toolkit.models import TestCase, Suite, TestResult

def run_test(test: TestCase) -> TestResult:

    response = httpx.request(test.request.method, test.request.url, json=test.request.data)
    errors: list[str] = []

    # check status
    if test.expected.status is not None:
        if response.status_code != test.expected.status:
            errors.append(
                f"status: expected {test.expected.status}, actual {response.status_code}"
            )
    
    # check json body
    if test.expected.json_body is not None:
        body = response.json()
        for key, expected_value in test.expected.json_body.items():
            if key not in body:
                errors.append(
                    f"json.{key}: key didn't exist in response"
                )
            elif body[key] != expected_value:
                errors.append(
                    f"json.{key}: expected {expected_value}, actual {body[key]}"
                )

    # check timer
    if test.expected.max_time_ms is not None:
        timer = response.elapsed.total_seconds() * 1000
        if timer > test.expected.max_time_ms:
            errors.append(
                f"time: expected <= {test.expected.max_time_ms}ms, actual {timer:.0f}ms"
            )

    return TestResult(name=test.name, errors=errors)


def run_suite(suite: Suite) -> list[TestResult]:
    return [run_test(test) for test in suite.tests]