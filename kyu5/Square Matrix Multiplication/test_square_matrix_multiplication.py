from asserts.Asserts import assert_true
import importlib

matrix_mult = importlib.import_module('kyu5.Square Matrix Multiplication.solution').matrix_mult


class TestSolution:
    def test_square_matrix_multiplication(self):
        assert_true(matrix_mult(
            [[1, 2],
             [3, 2]],
            #      x
            [[3, 2],
             [1, 1]]),
            #      =
            [[5, 4],
             [11, 8]])

        assert_true(matrix_mult(
            [[9, 7],
             [0, 1]],
            #      x
            [[1, 1],
             [4, 12]]),
            #      =
            [[37, 93],
             [4, 12]])

        assert_true(matrix_mult(
            [[1, 2, 3],
             [3, 2, 1],
             [2, 1, 3]],
            #       x
            [[4, 5, 6],
             [6, 5, 4],
             [4, 6, 5]]),
            #        =
            [[28, 33, 29],
             [28, 31, 31],
             [26, 33, 31]])

