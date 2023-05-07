import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import Case

solution = importlib.import_module('katas.8kyu.First non-consecutive number.solution').first_non_consecutive

cases = [
    Case([1, 2, 3, 4, 6, 7, 8], 6),
    Case([1, 2, 3, 4, 5, 6, 7, 8], None),
    Case([4, 6, 7, 8, 9, 11], 6),
    Case([4, 5, 6, 7, 8, 9, 11], 11),
    Case([31, 32], None),
    Case([-3, -2, 0, 1], 0),
    Case([-5, -4, -3, -1], -1),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_first_nonconsecutive_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
