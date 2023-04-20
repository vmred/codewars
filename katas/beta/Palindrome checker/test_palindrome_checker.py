import importlib

from asserts.asserts import assert_true

is_palindrome = importlib.import_module('katas.beta.Palindrome checker.solution').is_palindrome


class TestSolution:
    def test_palindrome_checker(self):
        assert_true(is_palindrome('Race Car'), True)
        # assert_true(is_palindrome('raccar'), True)
