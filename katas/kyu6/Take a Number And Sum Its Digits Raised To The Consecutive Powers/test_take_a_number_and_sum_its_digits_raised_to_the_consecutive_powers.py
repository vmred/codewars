from asserts.asserts import assert_true
import importlib

solution = importlib.import_module(
    'katas.kyu6.Take a Number And Sum Its Digits Raised To The Consecutive Powers.solution'
).sum_dig_pow


class TestSolution:
    def test_take_a_number_and_sum_its_digits_raised_to_the_consecutive_powers(self):
        assert_true(solution(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        assert_true(solution(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        assert_true(solution(10, 89), [89])
        assert_true(solution(10, 100), [89])
        assert_true(solution(90, 100), [])
        assert_true(solution(89, 135), [89, 135])
