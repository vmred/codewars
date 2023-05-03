import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.Valid Parentheses.solution').valid_parentheses

cases = [
    TestCase("  (", False),
    TestCase(")test", False),
    TestCase("", True),
    TestCase("hi())(", False),
    TestCase("hi(hi)()", True),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_valid_parentheses(self, test):
        assert_true(solution(test.test_data), test.test_output)
