import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Sort the odd.solution').sort_array

cases = [
    Case([5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4]),
    Case([5, 3, 1, 8, 0], [1, 3, 5, 8, 0]),
    Case([], []),
    Case([1, 111, 11, 11, 2, 1, 5, 0], [1, 1, 5, 11, 2, 11, 111, 0]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_sort_the_odd(self, test):
        assert_true(solution(test.test_data), test.test_output)
