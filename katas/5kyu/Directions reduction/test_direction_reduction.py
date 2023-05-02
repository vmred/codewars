import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.Directions reduction.solution').dirReduc

cases = [
    TestCase(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], ['WEST']),
    TestCase(["NORTH", "WEST", "SOUTH", "EAST"], ["NORTH", "WEST", "SOUTH", "EAST"]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_directions_reduction(self, test):
        assert_true(solution(test.test_data), test.test_output)
