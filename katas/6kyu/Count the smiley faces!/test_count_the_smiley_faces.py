import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Count the smiley faces!.solution').count_smileys

cases = [
    Case([], 0),
    Case([':D', ':~)', ';~D', ':)'], 4),
    Case([':)', ':(', ':D', ':O', ':;'], 2),
    Case([';]', ':[', ';*', ':$', ';-D'], 1),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_count_smiley_faces(self, test):
        assert_true(solution(test.test_data), test.test_output)
