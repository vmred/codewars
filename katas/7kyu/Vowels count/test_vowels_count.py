import importlib
from asserts.asserts import assert_true

getCount = importlib.import_module('katas.7kyu.Vowels count.solution').getCount


class TestSolution:
    def test_vowels_count(self):
        assert_true(getCount("abracadabra"), 5)
