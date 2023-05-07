import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.4kyu.Strip comments.solution').solution

cases = [
    Case(["apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]], "apples, pears\ngrapes\nbananas"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_strip_comments(self, test):
        assert_true(solution(*test.test_data), test.test_output)
