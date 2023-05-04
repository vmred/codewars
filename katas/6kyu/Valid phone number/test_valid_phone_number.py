import importlib
from asserts.asserts import assert_true

validPhoneNumber = importlib.import_module('katas.6kyu.Valid phone number.solution').validPhoneNumber


class TestSolution:
    def test_valid_phone_number(self):
        assert_true(validPhoneNumber("(123) 456-7890"), True)
