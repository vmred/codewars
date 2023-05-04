import importlib
from asserts.asserts import assert_true

square_digits = importlib.import_module('katas.7kyu.Square every digit.solution').square_digits


class TestSolution:
    def test_square_every_digit(self):
        assert_true(square_digits(9119), 811181)
