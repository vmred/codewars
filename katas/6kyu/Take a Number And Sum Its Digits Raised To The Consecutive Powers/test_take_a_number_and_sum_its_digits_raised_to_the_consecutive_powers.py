import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module(
    'katas.6kyu.Take a Number And Sum Its Digits Raised To The Consecutive Powers.solution'
).sum_dig_pow

cases = [
    Case([1, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    Case([1, 100], [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]),
    Case([10, 89], [89]),
    Case([10, 100], [89]),
    Case([90, 100], []),
    Case([89, 135], [89, 135]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_take_a_number_and_sum_its_digits_raised_to_the_consecutive_powers(self, test):
        assert_true(solution(*test.test_data), test.test_output)
