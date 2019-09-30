from asserts.Asserts import assert_true
import importlib

is_square = importlib.import_module('kyu7.You are a square.solution').is_square


class TestSolution:
    def test_you_are_a_square(self):
        assert_true(is_square(-1), False)
        assert_true(is_square(0), True)
        assert_true(is_square(3), False)
        assert_true(is_square(4), True)
        assert_true(is_square(25), True)
