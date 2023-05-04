import importlib
from asserts.asserts import assert_true

solution = importlib.import_module('katas.6kyu.Roman numerals encoder.solution').solution


class TestSolution:
    def test_roman_numerals_encoder(self):
        assert_true(solution(22), 'XXII')
        assert_true(solution(89), 'LXXXIX')
        assert_true(solution(1989), 'MCMLXXXIX')
