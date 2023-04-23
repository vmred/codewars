from asserts.asserts import assert_true
import importlib

longest = importlib.import_module('katas.6kyu.Longest alphabetical substring.solution').longest


class TestSolution:
    def test_longest_alphabetical_substring(self):
        assert_true(longest('nab'), 'ab')
        assert_true(longest('abcdeapbcdef'), 'abcde')
