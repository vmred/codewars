import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Sum two arrays.solution').sum_arrays

cases = [
    Case([[], []], []),
    Case([[3, 2, 9], [1, 2]], [3, 4, 1]),
    Case([[-3, 4, 2], [3, 4, 4]], [2]),
    Case([[0], []], [0]),
    Case([[-4, 9, 3, 1, 0], [2, 4]], [-4, 9, 2, 8, 6]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_sum_two_arrays(self, test):
        assert_true(solution(*test.test_data), test.test_output)
