from asserts.asserts import assert_true
import importlib

first_n_smallest = importlib.import_module('katas.kyu6.N smallest elements in original order.solution').first_n_smallest


class TestSolution:
    def test_n_smallest(self):
        assert_true(first_n_smallest([1, 2, 3, 4, 5], 3), [1, 2, 3])
        assert_true(first_n_smallest([5, 4, 3, 2, 1], 3), [3, 2, 1])
        assert_true(first_n_smallest([1, 2, 3, 1, 2], 3), [1, 2, 1])
        assert_true(first_n_smallest([1, 2, 3, -4, 0], 3), [1, -4, 0])
        assert_true(first_n_smallest([1, 2, 3, 4, 5], 0), [])
        assert_true(first_n_smallest([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        assert_true(first_n_smallest([1, 2, 3, 4, 2], 4), [1, 2, 3, 2])
        assert_true(first_n_smallest([2, 1, 2, 3, 4, 2], 2), [2, 1])
        assert_true(first_n_smallest([2, 1, 2, 3, 4, 2], 3), [2, 1, 2])
        assert_true(first_n_smallest([2, 1, 2, 3, 4, 2], 4), [2, 1, 2, 2])
