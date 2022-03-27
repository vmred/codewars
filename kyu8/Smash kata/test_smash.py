import importlib

from asserts.asserts import assert_true

smash = importlib.import_module('kyu8.Smash kata.solution').smash


class TestSolution:
    def test_permutations(self):
        assert_true(smash(['hello', 'world']), 'hello world')
