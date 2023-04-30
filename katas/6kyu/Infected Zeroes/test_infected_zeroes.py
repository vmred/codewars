import pytest
from asserts.asserts import assert_true
import importlib
from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Infected Zeroes.solution').infected_zeroes

cases = [
    TestCase([0], 0),
    TestCase([1, 1, 0, 1, 1], 2),
    TestCase([0, 1, 1, 1], 3),
]


class TestSolution:
    @pytest.mark.skip(reason='long tests not passed')
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_infected_zeroes(self, test):
        assert_true(solution(test.test_data), test.test_output)
