import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Maximum subarray sum.solution').max_sequence

cases = [
    Case([], 0),
    Case([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    Case([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43], 155),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_maximum_subarray_sum(self, test):
        assert_true(solution(test.test_data), test.test_output)
