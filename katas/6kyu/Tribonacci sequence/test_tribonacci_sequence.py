import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Tribonacci sequence.solution').tribonacci

cases = [
    Case([[1, 1, 1], 10], [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]),
    Case([[1, 1, 1], 1], [1]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_tribonacci_sequence(self, test):
        assert_true(solution(*test.test_data), test.test_output)
