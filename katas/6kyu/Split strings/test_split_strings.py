import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Split strings.solution').solution

cases = [
    Case('asdfadsf', ['as', 'df', 'ad', 'sf']),
    Case('asdfads', ['as', 'df', 'ad', 's_']),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_split_strings(self, test):
        assert_true(solution(test.test_data), test.test_output)
