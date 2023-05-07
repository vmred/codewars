import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Number of trailing zeros of n factorial.solution').zeros

cases = [
    Case(0, 0),
    Case(6, 1),
    Case(30, 7),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_numer_of_trailing_zeros_of_n_factorial(self, test):
        assert_true(solution(test.test_data), test.test_output)
