import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.4kyu.Sum of Intervals.solution').sum_of_intervals

cases = [
    TestCase([(1, 5)], 4),
    TestCase([(1, 5), (6, 10)], 8),
    TestCase([(1, 4), (7, 10), (3, 5)], 7),
    TestCase([(-1_000_000_000, 1_000_000_000)], 2_000_000_000),
    TestCase(
        [
            (-172, -21),
            (-431, 130),
            (-363, -59),
            (224, 430),
            (339, 374),
            (86, 385),
            (-447, -132),
            (195, 230),
            (195, 459),
            (47, 312),
        ],
        906,
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_sum_of_intervals(self, test):
        assert_true(solution(test.test_data), test.test_output)
