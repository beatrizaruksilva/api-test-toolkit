"""
Models Pydantic to define a test YAML file.

Expected -> expected return answer
Request -> how the request is setup
TestCase -> test = name + request + expected
Suite -> the whole file
"""

from pydantic import BaseModel, Field
from typing import Any


class Expected(BaseModel):
    status: int | None = None                          # optional
    json_body: dict | None = Field(default=None, alias="json")  # YAML usa "json", Python usa "json_body"
    max_time_ms: int | None = None                     # max time for response


class Request(BaseModel):
    method: str
    url: str
    data: dict[str, Any] | None = None


class TestCase(BaseModel):
    name: str
    request: Request
    expected: Expected


class Suite(BaseModel):
    tests: list[TestCase]


class TestResult(BaseModel):
    name: str
    errors: list[str] = []       # define assertion failed

    @property
    def passed(self) -> bool:
        return len(self.errors) == 0
