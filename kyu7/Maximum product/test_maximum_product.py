from asserts.Asserts import assert_true
import importlib

adjacent_element_product = importlib.import_module('kyu7.Maximum product.solution').adjacent_element_product


class TestSolution:
    def test_maximum_product(self):
        assert_true(adjacent_element_product([1, 5, 10, 9]), 90)
        assert_true(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]), -14)
