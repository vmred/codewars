import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.Josephus survivor.solution').josephus_survivor

cases = [
    TestCase([7, 3], 4),
    TestCase([11, 19], 10),
    TestCase([1, 300], 1),
    TestCase([14, 2], 13),
    TestCase([100, 1], 100),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_josephus_survivor(self, test):
        assert_true(solution(*test.test_data), test.test_output)
