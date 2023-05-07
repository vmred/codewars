import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Roman numerals decoder.solution').solution

cases = [
    Case('XXI', 21),
    Case('I', 1),
    Case('IV', 4),
    Case('MMVIII', 2008),
    Case('MDCLXVI', 1666),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_roman_numerals_decoder(self, test):
        assert_true(solution(test.test_data), test.test_output)
