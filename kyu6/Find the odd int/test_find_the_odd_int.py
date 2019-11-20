from asserts.Asserts import assert_true
import importlib

find_it = importlib.import_module('kyu6.Find the odd int.solution').find_it


class TestSolution:
    def test_find_the_odd_int(self):
        assert_true(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]), 5)
