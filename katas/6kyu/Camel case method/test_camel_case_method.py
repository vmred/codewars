import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Camel case method.solution').camel_case

cases = [
    TestCase('test case', 'TestCase'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_camel_case_method(self, test):
        assert_true(solution(test.test_data), test.test_output)
