from asserts.Asserts import assert_true
import importlib

group_ints = importlib.import_module('kyu6.Sorting Integers into a nested list.solution').group_ints


class TestSolution:
    def test_sorting_integers_into_a_nested_list(self):
        assert_true(group_ints([1, 2, 3], 3), [[1, 2], [3]])
        assert_true(group_ints([1, 3, 2], 3), [[1], [3], [2]])
