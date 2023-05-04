import importlib
from asserts.asserts import assert_true

is_square = importlib.import_module('katas.7kyu.You are a square.solution').is_square


class TestSolution:
    def test_you_are_a_square(self):
        assert_true(is_square(-1), False)
        assert_true(is_square(0), True)
        assert_true(is_square(3), False)
        assert_true(is_square(4), True)
        assert_true(is_square(25), True)
