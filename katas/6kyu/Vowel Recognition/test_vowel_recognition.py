import importlib
from asserts.asserts import assert_true

vowel_recognition = importlib.import_module('katas.6kyu.Vowel Recognition.solution').vowel_recognition


class TestSolution:
    def test_vowel_recognition(self):
        assert_true(vowel_recognition("baceb"), 16)
        assert_true(vowel_recognition("aeiouAEIOU"), 220)
