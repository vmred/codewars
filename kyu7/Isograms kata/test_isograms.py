from asserts.asserts import assert_true
import importlib

is_isogram = importlib.import_module('kyu7.Isograms kata.solution').is_isogram


class TestSolution:
    def test_isograms(self):
        assert_true(is_isogram("Dermatoglyphics"), True)
