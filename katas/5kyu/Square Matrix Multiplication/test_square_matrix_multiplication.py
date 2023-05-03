import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.Square Matrix Multiplication.solution').matrix_mult

cases = [
    TestCase([[[1, 2], [3, 2]], [[3, 2], [1, 1]]], [[5, 4], [11, 8]]),
    TestCase([[[9, 7], [0, 1]], [[1, 1], [4, 12]]], [[37, 93], [4, 12]]),
    TestCase(
        [[[1, 2, 3], [3, 2, 1], [2, 1, 3]], [[4, 5, 6], [6, 5, 4], [4, 6, 5]]],
        [[28, 33, 29], [28, 31, 31], [26, 33, 31]],
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_square_matrix_multiplication(self, test):
        assert_true(solution(*test.test_data), test.test_output)
