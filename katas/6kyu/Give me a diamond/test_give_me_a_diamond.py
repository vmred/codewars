import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Give me a diamond.solution').diamond

cases = [
    Case(1, "*\n"),
    Case(2, None),
    Case(3, ' *\n***\n *\n'),
    Case(5, '  *\n ***\n*****\n ***\n  *\n'),
    Case(0, None),
    Case(-3, None),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_give_me_a_diamond(self, test):
        assert_true(solution(test.test_data), test.test_output)
