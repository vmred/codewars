import importlib

from asserts.asserts import assert_true

binary_array_to_number = importlib.import_module('katas.7kyu.Ones and zeros.solution').binary_array_to_number


class TestSolution:
    def test_binary_array_to_number(self):
        assert_true(binary_array_to_number([0, 0, 0, 1]), 1)
        assert_true(binary_array_to_number([0, 0, 1, 0]), 2)
        assert_true(binary_array_to_number([1, 1, 1, 1]), 15)
        assert_true(binary_array_to_number([0, 1, 1, 0]), 6)
