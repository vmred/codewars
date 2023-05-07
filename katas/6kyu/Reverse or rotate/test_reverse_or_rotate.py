import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Reverse or rotate.solution').revrot

cases = [
    Case(["3304991787281570455176064327690480265895", 8], '1994033775182780067155464327690480265895'),
]


class TestSolution:
    @pytest.mark.not_completed
    @pytest.mark.xfail
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_reverse_or_rotate(self, test):
        assert_true(solution(*test.test_data), test.test_output)
