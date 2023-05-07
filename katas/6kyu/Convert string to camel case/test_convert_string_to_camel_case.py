import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Convert string to camel case.solution').to_camel_case

cases = [
    Case("the_stealth_warrior", 'theStealthWarrior'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_convert_string_to_camel_case(self, test):
        assert_true(solution(test.test_data), test.test_output)
