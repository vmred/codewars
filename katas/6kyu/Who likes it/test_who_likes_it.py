import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Who likes it.solution').likes

cases = [
    Case([[]], 'no one likes this'),
    Case([['Peter']], 'Peter likes this'),
    Case([['Jacob', 'Alex']], 'Jacob and Alex like this'),
    Case([['Max', 'John', 'Mark']], 'Max, John and Mark like this'),
    Case([['Alex', 'Jacob', 'Mark', 'Max']], 'Alex, Jacob and 2 others like this'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_who_likes_it(self, test):
        assert_true(solution(*test.test_data), test.test_output)
