from asserts.Asserts import assert_true
import importlib

array_diff = importlib.import_module('kyu6.Array diff.solution').array_diff


class TestSolution:
    def test_array_diff(self):
        assert_true(array_diff([1, 2], [1]), [2])
        assert_true(array_diff([1, 2, 2], []), [1, 2, 2])
