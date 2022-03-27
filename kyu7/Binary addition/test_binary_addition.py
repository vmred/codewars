from asserts.asserts import assert_true
import importlib

add_binary = importlib.import_module('kyu7.Binary addition.solution').add_binary


class TestSolution:
    def test_binary_addition(self):
        assert_true(add_binary(1, 1), "10")
        assert_true(add_binary(0, 1), "1")
        assert_true(add_binary(1, 0), "1")
        assert_true(add_binary(2, 2), "100")
        assert_true(add_binary(51, 12), "111111")
