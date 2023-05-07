import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.First non-repeating character.solution').first_non_repeating_letter

cases = [
    Case('a', 'a'),
    Case('stress', 't'),
    Case('moonmen', 'e'),
    Case('', ''),
    Case('hello world, eh?', 'w'),
    Case('sTreSS', 'T'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_first_non_repeating_char(self, test):
        assert_true(solution(test.test_data), test.test_output)
