import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.First non-consecutive number.solution').first_non_consecutive

cases = [
    TestCase([1, 2, 3, 4, 6, 7, 8], 6),
    TestCase([1, 2, 3, 4, 5, 6, 7, 8], None),
    TestCase([4, 6, 7, 8, 9, 11], 6),
    TestCase([4, 5, 6, 7, 8, 9, 11], 11),
    TestCase([31, 32], None),
    TestCase([-3, -2, 0, 1], 0),
    TestCase([-5, -4, -3, -1], -1),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_first_nonconsecutive_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
