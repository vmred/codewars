from asserts.asserts import assert_true
import importlib

product_array = importlib.import_module('katas.kyu7.Product array.solution').product_array


class TestSolution:
    def test_product_array(self):
        assert_true(product_array([3, 27, 4, 2]), [216, 24, 162, 324])
        assert_true(product_array([16, 17, 4, 3, 5, 2]), [2040, 1920, 8160, 10880, 6528, 16320])
