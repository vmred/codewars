import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Roman numerals encoder.solution').solution

cases = [
    Case(22, 'XXII'),
    Case(89, 'LXXXIX'),
    Case(1989, 'MCMLXXXIX'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_roman_numerals_encoder(self, test):
        assert_true(solution(test.test_data), test.test_output)
