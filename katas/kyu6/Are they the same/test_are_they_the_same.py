from asserts.asserts import assert_true
import importlib

comp = importlib.import_module('katas.kyu6.Are they the same.solution').comp


class TestSolution:
    def test_are_they_the_same(self):
        assert_true(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]), True)
        assert_true(comp([10, 99], [101, 9801]), False)
        assert_true(comp([], []), True)
