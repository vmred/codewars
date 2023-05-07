import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Build a pile of cubes.solution').find_nb

cases = [
    Case(4183059834009, 2022),
    Case(24723578342962, -1),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_build_a_pile_of_cubes(self, test):
        assert_true(solution(test.test_data), test.test_output)
