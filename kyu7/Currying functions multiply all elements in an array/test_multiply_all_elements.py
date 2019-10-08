from asserts.Asserts import assert_true
import importlib

multiply_all = importlib.import_module(
    'kyu7.Currying functions multiply all elements in an array.solution').multiply_all


class TestSolution:
    def test_multiply_all_elements_in_array(self):
        assert_true(multiply_all([1, 2, 3])(1), [1, 2, 3])
        assert_true(multiply_all([1, 2, 3])(2), [2, 4, 6])
        assert_true(multiply_all([1, 2, 3])(0), [0, 0, 0])
        assert_true(multiply_all([])(10), [])
