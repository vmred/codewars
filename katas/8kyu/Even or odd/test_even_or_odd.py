import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.8kyu.Even or odd.solution').even_or_odd

cases = [
    Case(2, "Even"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_even_or_odd(self, test):
        assert_true(solution(test.test_data), test.test_output)
