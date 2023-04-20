from asserts.asserts import assert_true
import importlib

validate = importlib.import_module('katas.kyu6.Validate credit card number.solution').validate


class TestSolution:
    def test_validate_credit_card_number(self):
        assert_true(validate(123), False)
        assert_true(validate(1), False)
        assert_true(validate(2121), True)
        assert_true(validate(1230), True)
