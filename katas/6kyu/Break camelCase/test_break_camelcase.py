import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Break camelCase.solution').solution

cases = [
    TestCase("helloWorld", "hello World"),
    TestCase("camelCase", "camel Case"),
    TestCase('breakCamelCase', 'break Camel Case'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_break_camelcase(self, test):
        assert_true(solution(test.test_data), test.test_output)
