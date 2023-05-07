import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Dont rely on luck.solution').randint
guess = importlib.import_module('katas.6kyu.Dont rely on luck.solution').guess

cases = [
    Case([1, 100], guess),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_dont_rely_on_luck(self, test):
        assert_true(solution(test.test_data), test.test_output)
