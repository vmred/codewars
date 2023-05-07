import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.4kyu.Calculate kth digit of Pi.solution').pi

cases = [
    TestCase(0, 3),
    TestCase(1, 1),
    TestCase(6, 2),
    TestCase(1001, 3),
    TestCase(9999, 7)
]


class TestSolution:

    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_calculate_kth_digit_of_pi(self, test):
        assert_true(solution(test.test_data), test.test_output)
