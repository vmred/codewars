import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.4kyu.Explosive sum.solution').exp_sum

cases = [
    Case(1, 1),
    Case(2, 2),
    Case(3, 3),
    Case(4, 5),
    Case(5, 7),
    Case(10, 42),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_explosive_sum(self, test):
        assert_true(solution(test.test_data), test.test_output)
