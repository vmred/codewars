import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.The hashtag generator.solution').generate_hashtag

cases = [
    Case('', False),
    Case('Codewars', '#Codewars'),
    Case('Codewars         ', '#Codewars'),
    Case('CodeWars is nice', '#CodewarsIsNice'),
    Case('c i n', '#CIN'),
    Case(
        'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
        'oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat',
        False,
    ),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_hashtag_generator(self, test):
        assert_true(solution(test.test_data), test.test_output)

    def test_hashtag_generator_corner_case(self):
        assert_true(solution('Do We have A Hashtag')[0], '#')
