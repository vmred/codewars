import importlib

from asserts.asserts import assert_true

basic_op = importlib.import_module('kyu8.Basic mathematical operations.solution').basic_op


class TestSolution:
    def test_basic_mathematical_operations(self):
        assert_true(basic_op('+', 4, 7), 11)
        assert_true(basic_op('-', 15, 18), -3)
        assert_true(basic_op('*', 5, 5), 25)
        assert_true(basic_op('/', 49, 7), 7)
