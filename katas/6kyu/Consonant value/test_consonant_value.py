import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Consonant value.solution').solve

cases = [
    Case("zodiac", 26),
    Case("strength", 57),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_consonant_value(self, test):
        assert_true(solution(test.test_data), test.test_output)
