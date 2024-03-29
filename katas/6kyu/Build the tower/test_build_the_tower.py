import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Build the tower.solution').tower_builder

cases = [
    Case(1, ['*']),
    Case(3, ['  *  ', ' *** ', '*****']),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_build_the_tower(self, test):
        assert_true(solution(test.test_data), test.test_output)
