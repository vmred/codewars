import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Build a pile of cubes.solution').find_nb

cases = [
    TestCase(4183059834009, 2022),
    TestCase(24723578342962, -1),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_build_a_pile_of_cubes(self, test):
        assert_true(solution(test.test_data), test.test_output)
