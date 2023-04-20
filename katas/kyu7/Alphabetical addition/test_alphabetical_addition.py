import importlib

from asserts.asserts import assert_true

add_letters = importlib.import_module('katas.kyu7.Alphabetical addition.solution').add_letters


class TestSolution:
    def test_alphabet_addition(self):
        assert_true(add_letters('a', 'b', 'c'), 'f')
        assert_true(add_letters('z', 'a'), 'a')
        assert_true(add_letters("u", "n", "e", "v"), 'j')
