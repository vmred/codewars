import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Shortest steps to a number.solution').shortest_steps_to_num

cases = [Case(16, 4), Case(71, 9)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_shortest_steps_to_a_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
