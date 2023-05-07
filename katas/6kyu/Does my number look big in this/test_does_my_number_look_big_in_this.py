import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Does my number look big in this.solution').narcissistic

cases = [
    Case(371, True),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_does_my_number_look_big_in_this(self, test):
        assert_true(solution(test.test_data), test.test_output)
