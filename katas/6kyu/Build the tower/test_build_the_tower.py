import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Build the tower.solution').tower_builder

cases = [
    TestCase(1, ['*']),
    TestCase(3, ['  *  ', ' *** ', '*****']),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_build_the_tower(self, test):
        assert_true(solution(test.test_data), test.test_output)
