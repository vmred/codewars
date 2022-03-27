from asserts.asserts import assert_true
import importlib

vowel_recognition = importlib.import_module('kyu6.Vowel Recognition.solution').vowel_recognition


class TestSolution:
    def test_vowel_recognition(self):
        assert_true(vowel_recognition("baceb"), 16)
        assert_true(vowel_recognition("aeiouAEIOU"), 220)
