from asserts.asserts import assert_true
import importlib

solution = importlib.import_module('kyu6.Roman numerals encoder.solution').solution


class TestSolution:
    def test_roman_numerals_encoder(self):
        assert_true(solution(22), 'XXII')
        assert_true(solution(89), 'LXXXIX')
        assert_true(solution(1989), 'MCMLXXXIX')
