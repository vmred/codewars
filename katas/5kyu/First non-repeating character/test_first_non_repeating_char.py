import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.First non-repeating character.solution').first_non_repeating_letter

cases = [
    TestCase('a', 'a'),
    TestCase('stress', 't'),
    TestCase('moonmen', 'e'),
    TestCase('', ''),
    TestCase('hello world, eh?', 'w'),
    TestCase('sTreSS', 'T'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_first_non_repeating_char(self, test):
        assert_true(solution(test.test_data), test.test_output)
