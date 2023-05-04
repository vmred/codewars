import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.4kyu.Counting Change Combinations.solution').count_change

cases = [
    TestCase([4, [1, 2]], 3),
    TestCase([10, [5, 2, 3]], 4),
    TestCase([1116, [2, 212, 494, 73, 335]], 61),
    TestCase([886, [245, 30, 356, 97, 158]], 3),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_counting_change_combinations(self, test):
        assert_true(solution(*test.test_data), test.test_output)
