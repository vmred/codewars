import importlib
from asserts.asserts import assert_true

is_triangle = importlib.import_module('katas.7kyu.Is this a triangle.solution').is_triangle


class TestSolution:
    def test_is_this_a_triangle(self):
        assert_true(is_triangle(1, 2, 2), True)
        assert_true(is_triangle(7, 2, 2), False)
