import httpx
from api_test_toolkit.models import TestCase, Suite, TestResult

def run_test(test: TestCase) -> TestResult:

    response = httpx.request(test.request.method, test.request.url, json=test.request.data)
    passed = response.status_code == test.expected.status
    return TestResult(
        name=test.name,
        passed=passed,
        expected_status=test.expected.status,
        actual_status=response.status_code
    )

def run_suite(suite: Suite) -> list[TestResult]:
    return [run_test(test) for test in suite.tests]