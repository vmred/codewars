import importlib

from asserts.Asserts import assert_true

anagrams = importlib.import_module('kyu5.Where my anagrams at.solution').anagrams


class TestSolution:
    def test_where_my_anagrams_at(self):
        assert_true(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        assert_true(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
