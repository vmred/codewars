from asserts.Asserts import assert_true
import importlib

digitize = importlib.import_module('kyu8.Convert number to reversed array of digits.solution').digitize


class TestSolution:
    def test_convert_number_to_reversed_array_of_digits(self):
        assert_true(digitize(35231), [1, 3, 2, 5, 3])
