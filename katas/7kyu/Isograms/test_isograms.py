import importlib
from asserts.asserts import assert_true

is_isogram = importlib.import_module('katas.7kyu.Isograms.solution').is_isogram


class TestSolution:
    def test_isograms(self):
        assert_true(is_isogram("Dermatoglyphics"), True)
