import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Format a string of names.solution').namelist

cases = [
    Case([[{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]], 'Bart, Lisa & Maggie'),
    Case([[{'name': 'Bart'}]], 'Bart'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_format_a_string_of_names(self, test):
        assert_true(solution(*test.test_data), test.test_output)
