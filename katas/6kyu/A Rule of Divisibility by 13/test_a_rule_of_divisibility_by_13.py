import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import TestCase


solution = importlib.import_module('katas.6kyu.A Rule of Divisibility by 13.solution').thirt


cases = [
    TestCase(8529, 79),
    TestCase(1234567, 87),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_a_rule_of_divisibility_by_13(self, test):
        assert_true(solution(test.test_data), test.test_output)
