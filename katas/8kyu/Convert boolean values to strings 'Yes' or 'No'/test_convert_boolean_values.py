import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

sol = importlib.import_module('katas.8kyu.Convert boolean values to strings \'Yes\' or \'No\'.solution').bool_to_word

cases = [
    TestCase(True, 'Yes'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_convert_boolean_values_to_strings_yes_or_no(self, test):
        assert_true(sol(test.test_data), test.test_output)
