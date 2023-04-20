import importlib

from asserts.asserts import assert_true

remove_smallest = importlib.import_module('katas.kyu7.Remove the minimum.solution').remove_smallest


class TestSolution:
    def test_remove_the_minimum(self):
        assert_true(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])
        assert_true(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])
        assert_true(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1])
