import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Good vs Evil.solution').goodVsEvil

cases = [
    Case(['1 1 1 1 1 1', '1 1 1 1 1 1 1'], 'Battle Result: Evil eradicates all trace of Good'),
    Case(['441 856 420 152 146 622', '823 86 367 77 464 304 551'], 'Battle Result: Good triumphs over Evil'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_good_vs_evil(self, test):
        assert_true(solution(*test.test_data), test.test_output)
