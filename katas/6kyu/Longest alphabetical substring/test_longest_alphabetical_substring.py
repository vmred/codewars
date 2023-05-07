import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Longest alphabetical substring.solution').longest

cases = [Case('nab', 'ab'), Case('abcdeapbcdef', 'abcde')]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_longest_alphabetical_substring(self, test):
        assert_true(solution(test.test_data), test.test_output)
