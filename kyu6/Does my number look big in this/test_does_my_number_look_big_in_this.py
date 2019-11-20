from asserts.Asserts import assert_true
import importlib

narcissistic = importlib.import_module('kyu6.Does my number look big in this.solution').narcissistic


class TestSolution:
    def test_does_my_number_look_big_in_this(self):
        assert_true(narcissistic(371), True)
