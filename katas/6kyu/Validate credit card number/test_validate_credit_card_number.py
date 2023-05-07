import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Validate credit card number.solution').validate

cases = [
    Case(123, False),
    Case(1, False),
    Case(2121, True),
    Case(1230, True),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_validate_credit_card_number(self, test):
        assert_true(solution(test.test_data), test.test_output)
