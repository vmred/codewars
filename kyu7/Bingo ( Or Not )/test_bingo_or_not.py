from asserts.Asserts import assert_true
import importlib

bingo = importlib.import_module('kyu7.Bingo ( Or Not ).solution').bingo


class TestSolution:
    def test_bingo_or_not(self):
        assert_true(bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "LOSE")
        assert_true(bingo([20, 12, 23, 14, 6, 22, 12, 17, 2, 26]), "LOSE")
        assert_true(bingo([1, 2, 3, 7, 5, 14, 7, 15, 9, 10]), "WIN")
        assert_true(bingo([5, 2, 13, 7, 5, 14, 17, 15, 9, 10]), "WIN")
