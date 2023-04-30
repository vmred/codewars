import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Sum of positive.solution').positive_sum

cases = [
    TestCase([-1, 2, 3, 4, -5], 9),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_sum_of_positive(self, test):
        assert_true(solution(test.test_data), test.test_output)
