import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Dashatize it.solution').dashatize

cases = [
    Case(274, "2-7-4"),
    Case(86320, "86-3-20"),
    Case(-1, '1'),
    Case(0, '0'),
    Case(None, 'None'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_dashatize_it(self, test):
        assert_true(solution(test.test_data), test.test_output)
