from asserts.asserts import assert_true
import importlib

diamond = importlib.import_module('kyu6.Give me a diamond.solution').diamond


class TestSolution:
    def test_give_me_a_diamond(self):
        assert_true(diamond(1), "*\n")
        assert_true(diamond(2), None)
        assert_true(diamond(3), " *\n***\n *\n")
        assert_true(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
        assert_true(diamond(0), None)
        assert_true(diamond(-3), None)
