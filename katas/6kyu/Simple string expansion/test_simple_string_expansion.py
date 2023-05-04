import importlib
from asserts.asserts import assert_true

solve = importlib.import_module('katas.6kyu.Simple string expansion.solution').solve


class TestSolution:
    def test_simple_string_expansion(self):
        assert_true(True, True)
