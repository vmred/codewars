from asserts.asserts import assert_true
import importlib

find_outlier = importlib.import_module('katas.kyu6.Find the parity outlier.solution').find_outlier


class TestSolution:
    def test_find_the_parity_outlier(self):
        assert_true(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        assert_true(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
