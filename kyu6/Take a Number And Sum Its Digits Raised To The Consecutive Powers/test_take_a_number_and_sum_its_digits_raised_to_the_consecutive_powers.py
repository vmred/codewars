from asserts.Asserts import assert_true
import importlib

sum_dig_pow = importlib.import_module(
    'kyu6.Take a Number And Sum Its Digits Raised To The Consecutive Powers.solution').sum_dig_pow


class TestSolution:
    def test_take_a_number_and_sum_its_digits_raised_to_the_consecutive_powers(self):
        assert_true(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert_true(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        assert_true(sum_dig_pow(10, 89), [89])
        assert_true(sum_dig_pow(10, 100), [89])
        assert_true(sum_dig_pow(90, 100), [])
        assert_true(sum_dig_pow(89, 135), [89, 135])