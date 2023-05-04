import importlib
from asserts.asserts import assert_true

find_even_index = importlib.import_module('katas.6kyu.Equal sides of an array.solution').find_even_index


class TestSolution:
    def test_equal_sides_of_an_array(self):
        assert_true(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
        assert_true(find_even_index([1, 2, 3, 4, 5, 6]), -1)
        assert_true(find_even_index([20, 10, -80, 10, 10, 15, 35]), 0)
