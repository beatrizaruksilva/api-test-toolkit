import httpx
from api_test_toolkit.models import TestCase, Suite

def run_test(test: TestCase) -> str:

    response = httpx.request(test.request.method, test.request.url, json=test.request.data)
    is_valid = response.status_code == test.expected.status
    return f"{test.name} {"passou" if is_valid else "falhou"}"

def run_suite(suite: Suite) -> str:
    result = ""
    for test in suite.tests:
        result += f"{run_test(test)} \n"
    return result