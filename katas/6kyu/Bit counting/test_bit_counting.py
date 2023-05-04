import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Bit counting.solution').countBits

cases = [
    TestCase(10, 2),
    TestCase(1, 1),
    TestCase(0, 0),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_bit_counting(self, test):
        assert_true(solution(test.test_data), test.test_output)
