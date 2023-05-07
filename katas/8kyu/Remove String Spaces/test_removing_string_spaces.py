import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.8kyu.Remove String Spaces.solution').no_space

cases = [
    Case('8 j 8   mBliB8g  imjB8B8  jl  B', '8j8mBliB8gimjB8B8jlB'),
    Case('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd', '88Bifk8hB8BB8BBBB888chl8BhBfd'),
    Case('8aaaaa dddd r     ', '8aaaaaddddr'),
    Case('jfBm  gk lf8hg  88lbe8 ', 'jfBmgklf8hg88lbe8'),
    Case('8j aam', '8jaam'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_remove_string_spaces(self, test):
        assert_true(solution(test.test_data), test.test_output)
