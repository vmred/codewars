from asserts.asserts import assert_true
import importlib

solution = importlib.import_module('katas.6kyu.Length of missing array.solution').get_length_of_missing_array


class TestSolution:
    def test_length_of_missing_array(self):
        assert_true(solution([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 3)
        assert_true(solution([None, [1, 2]]), 0)
