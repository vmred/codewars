import importlib
from asserts.asserts import assert_true

create_phone_number = importlib.import_module('katas.6kyu.Create phone number.solution').create_phone_number


class TestSolution:
    def test_create_phone_number(self):
        assert_true(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), '(123) 456-7890')
        assert_true(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
