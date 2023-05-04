import importlib
from asserts.asserts import assert_true

max_pizza = importlib.import_module('katas.6kyu.Pizza pieces.solution').max_pizza


class TestSolution:
    def test_pizza_pieces(self):
        assert_true(max_pizza(3), 7)
        assert_true(max_pizza(4), 11)
