import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Getting started #lets piay.solution').whatpimeans

cases = [
    Case('no args', 'THANKYOU'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_getting_started_lets_piay(self, test):
        actual = test.test_data != 'no args' and solution(test.test_data) or solution()
        assert_true(actual, test.test_output)
