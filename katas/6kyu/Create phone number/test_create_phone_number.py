import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Create phone number.solution').create_phone_number

cases = [
    Case([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], '(123) 456-7890'),
    Case([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], '(111) 111-1111'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_create_phone_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
