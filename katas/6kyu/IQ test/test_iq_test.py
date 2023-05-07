import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.IQ test.solution').iq_test

cases = [
    Case("2 4 7 8 10", 3),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_iq_test(self, test):
        assert_true(solution(test.test_data), test.test_output)
