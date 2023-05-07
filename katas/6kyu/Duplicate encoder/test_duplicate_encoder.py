import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Duplicate encoder.solution').duplicate_encode

cases = [Case('recede', '()()()'), Case('Supralapsarian', ')()))()))))()(')]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_duplicate_encoder(self, test):
        assert_true(solution(test.test_data), test.test_output)
