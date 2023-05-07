import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Sum of parts.solution').parts_sums

cases = [
    Case([], [0]),
    Case([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_sum_of_parts(self, test):
        assert_true(solution(test.test_data), test.test_output)
