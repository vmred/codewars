import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Reverse or rotate.solution').revrot

cases = [
    Case(["3304991787281570455176064327690480265895", 8], '7199403307518278606715543276904402658958'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_reverse_or_rotate(self, test):
        assert_true(solution(*test.test_data), test.test_output)
