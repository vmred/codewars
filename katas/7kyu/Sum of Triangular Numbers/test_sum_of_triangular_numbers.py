from asserts.asserts import assert_true
import importlib

sum_triangular_numbers = importlib.import_module('katas.7kyu.Sum of Triangular Numbers.solution').sum_triangular_numbers


class TestSolution:
    def test_sum_of_triangular_numbers(self):
        assert_true(sum_triangular_numbers(6), 56)
        assert_true(sum_triangular_numbers(34), 7140)
        assert_true(sum_triangular_numbers(-291), 0)
        assert_true(sum_triangular_numbers(943), 140205240)
        assert_true(sum_triangular_numbers(-971), 0)
