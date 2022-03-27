from asserts.asserts import assert_true
import importlib

validPhoneNumber = importlib.import_module('kyu6.Valid phone number.solution').validPhoneNumber


class TestSolution:
    def test_valid_phone_number(self):
        assert_true(validPhoneNumber("(123) 456-7890"), True)
