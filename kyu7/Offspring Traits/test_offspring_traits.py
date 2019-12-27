from asserts.Asserts import assert_true
import importlib

bear_fur = importlib.import_module('kyu7.Offspring Traits.solution').bear_fur


class TestSolution:
    def test_offspring_traits(self):
        assert_true(bear_fur(['black', 'black']), 'black')
        assert_true(bear_fur(['green', 'brown']), 'unknown')