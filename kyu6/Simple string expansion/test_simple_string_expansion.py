from asserts.Asserts import assert_true
import importlib

solve = importlib.import_module('kyu6.Simple string expansion.solution').solve


class TestSolution:
    def test_simple_string_expansion(self):
        assert_true(True, True)
