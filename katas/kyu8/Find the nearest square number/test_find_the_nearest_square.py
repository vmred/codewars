from asserts.asserts import assert_true
import importlib

nearest_sq = importlib.import_module('katas.kyu8.Find the nearest square number.solution').nearest_sq


class TestSolution:
    def test_find_the_nearest_square_number(self):
        assert_true(nearest_sq(111), 121)
