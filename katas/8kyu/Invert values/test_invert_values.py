import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Invert values.solution').invert

cases = [
    TestCase([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]),
    TestCase([1, -2, 3, -4, 5], [-1, 2, -3, 4, -5]),
    TestCase([], []),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_invert_values(self, test):
        assert_true(solution(test.test_data), test.test_output)
