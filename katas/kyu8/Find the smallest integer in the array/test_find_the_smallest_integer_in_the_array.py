import importlib

from asserts.asserts import assert_true

find_smallest_int = importlib.import_module('katas.kyu8.Find the smallest integer in the array.solution').find_smallest_int


class TestSolution:
    def test_find_the_smallest_in_the_array(self):
        assert_true(find_smallest_int([0, 1 - 2 ** 64, 2 ** 64]), 1 - 2 ** 64)
