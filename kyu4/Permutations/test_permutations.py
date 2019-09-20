import importlib

from asserts.Asserts import assert_true

permutations = importlib.import_module('kyu4.Permutations.solution').permutations


class TestSolution:
    def test_permutations(self):
        assert_true(sorted(permutations('a')), ['a'])
        assert_true(sorted(permutations('ab')), ['ab', 'ba'])
        assert_true(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
