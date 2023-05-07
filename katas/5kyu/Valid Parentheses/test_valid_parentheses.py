import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Valid Parentheses.solution').valid_parentheses

cases = [
    Case("  (", False),
    Case(")test", False),
    Case("", True),
    Case("hi())(", False),
    Case("hi(hi)()", True),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_valid_parentheses(self, test):
        assert_true(solution(test.test_data), test.test_output)
