import importlib

from asserts.asserts import assert_true

flatten_and_sort = importlib.import_module('kyu7.Flatten and sort array.solution').flatten_and_sort


class TestSolution:
    def test_flatten_and_sort_array(self):
        assert_true(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
