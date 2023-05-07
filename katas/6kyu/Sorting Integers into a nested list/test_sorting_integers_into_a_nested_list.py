import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Sorting Integers into a nested list.solution').group_ints

cases = [
    Case([[1, 2, 3], 3], [[1, 2], [3]]),
    Case([[1, 3, 2], 3], [[1], [3], [2]]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_sorting_integers_into_a_nested_list(self, test):
        assert_true(solution(*test.test_data), test.test_output)
