import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Character frequency.solution').letter_frequency

cases = [
    Case(
        'wklv lv d vhfuhw phvvdjh',
        [('v', 5), ('h', 4), ('d', 2), ('l', 2), ('w', 2), ('f', 1), ('j', 1), ('k', 1), ('p', 1), ('u', 1)],
    ),
    Case(
        'As long as I\'m learning something, I figure I\'m OK - it\'s a decent day.',
        [
            ('i', 7),
            ('a', 5),
            ('e', 5),
            ('n', 5),
            ('g', 4),
            ('s', 4),
            ('m', 3),
            ('o', 3),
            ('t', 3),
            ('d', 2),
            ('l', 2),
            ('r', 2),
            ('c', 1),
            ('f', 1),
            ('h', 1),
            ('k', 1),
            ('u', 1),
            ('y', 1),
        ],
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_character_frequency(self, test):
        assert_true(solution(test.test_data), test.test_output)
