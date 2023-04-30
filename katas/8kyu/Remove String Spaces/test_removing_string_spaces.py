import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.8kyu.Remove String Spaces.solution').no_space

cases = [
    TestCase('8 j 8   mBliB8g  imjB8B8  jl  B', '8j8mBliB8gimjB8B8jlB'),
    TestCase('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd', '88Bifk8hB8BB8BBBB888chl8BhBfd'),
    TestCase('8aaaaa dddd r     ', '8aaaaaddddr'),
    TestCase('jfBm  gk lf8hg  88lbe8 ', 'jfBmgklf8hg88lbe8'),
    TestCase('8j aam', '8jaam'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_remove_string_spaces(self, test):
        assert_true(solution(test.test_data), test.test_output)
