import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Backspaces in string.solution').clean_string

cases = [
    Case('abc#d##c', 'ac'),
    Case('abc####d##c#', ''),
    Case("", ''),
    Case('w#h##E##b#9[z0,##', '9[z'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_backspaces_in_string(self, test):
        assert_true(solution(test.test_data), test.test_output)
