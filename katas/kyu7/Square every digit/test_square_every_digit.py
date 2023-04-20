from asserts.asserts import assert_true
import importlib

square_digits = importlib.import_module('katas.kyu7.Square every digit.solution').square_digits


class TestSolution:
    def test_square_every_digit(self):
        assert_true(square_digits(9119), 811181)
