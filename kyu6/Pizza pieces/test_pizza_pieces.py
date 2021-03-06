from asserts.Asserts import assert_true
import importlib

max_pizza = importlib.import_module('kyu6.Pizza pieces.solution').max_pizza


class TestSolution:
    def test_pizza_pieces(self):
        assert_true(max_pizza(3), 7)
        assert_true(max_pizza(4), 11)
