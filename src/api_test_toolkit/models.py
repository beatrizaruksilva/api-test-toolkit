"""
Models Pydantic to define a test YAML file.

Expected -> expected return answer
Request -> how the request is setup
TestCase -> test = name + request + expected
Suite -> the whole file
"""

from pydantic import BaseModel
from typing import Any


class Expected(BaseModel):
    status: int


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
