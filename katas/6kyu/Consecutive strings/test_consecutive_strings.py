import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Consecutive strings.solution').longest_consec

cases = [
    Case([["zone", "abigail", "theta", "form", "libe", "zas"], 2], 'abigailtheta'),
    Case([['wlwsasphmxx', 'owiaxujylentrklctozmymu', 'wpgozvxxiu'], 2], 'wlwsasphmxxowiaxujylentrklctozmymu'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_consecutive_strings(self, test):
        assert_true(solution(*test.test_data), test.test_output)
