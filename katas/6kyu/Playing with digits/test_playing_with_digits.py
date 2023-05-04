import importlib
from asserts.asserts import assert_true

dig_pow = importlib.import_module('katas.6kyu.Playing with digits.solution').dig_pow


class TestSolution:
    def test_playing_with_digits(self):
        assert_true(dig_pow(46288, 3), 51)
