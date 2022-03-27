from asserts.asserts import assert_true
import importlib

getCount = importlib.import_module('kyu7.Vowels count.solution').getCount


class TestSolution:
    def test_vowels_count(self):
        assert_true(getCount("abracadabra"), 5)
