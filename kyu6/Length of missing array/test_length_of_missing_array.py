from asserts.Asserts import assert_true
import importlib

get_length_of_missing_array = importlib.import_module(
    'kyu6.Length of missing array.solution').get_length_of_missing_array


class TestSolution:
    def test_length_of_missing_array(self):
        assert_true(get_length_of_missing_array([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 3)
        assert_true(get_length_of_missing_array([None, [1, 2]]), 0)
