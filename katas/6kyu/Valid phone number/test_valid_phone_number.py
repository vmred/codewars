import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Valid phone number.solution').validPhoneNumber

cases = [
    Case('(123) 456-7890', True),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_valid_phone_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
