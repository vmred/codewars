from asserts.Asserts import assert_true
import importlib

find_next_square = importlib.import_module('kyu7.Find the next perfect square.solution').find_next_square


class TestSolution:
    def test_find_next_perfect_square(self):
        assert_true(find_next_square(114), -1)
        assert_true(find_next_square(121), 144)
