from asserts.asserts import assert_true
import importlib

find_uniq = importlib.import_module('katas.6kyu.Find the unique number.solution').find_uniq


class TestSolution:
    def test_find_the_unique_number(self):
        assert_true(find_uniq([1, 1, 1, 2, 1, 1]), 2)
        assert_true(find_uniq([3, 4, 4, 4, 4, 4, 4, 4]), 3)
