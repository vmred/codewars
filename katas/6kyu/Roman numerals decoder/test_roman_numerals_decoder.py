import importlib

from asserts.asserts import assert_true

solution = importlib.import_module('katas.6kyu.Roman numerals decoder.solution').solution


class TestSolution:
    def test_roman_numerals_decoder(self):
        assert_true(solution('XXI'), 21)
        assert_true(solution('I'), 1)
        assert_true(solution('IV'), 4)
        assert_true(solution('MMVIII'), 2008)
        assert_true(solution('MDCLXVI'), 1666)
