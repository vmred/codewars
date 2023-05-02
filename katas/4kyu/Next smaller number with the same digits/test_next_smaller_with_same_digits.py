import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.4kyu.Next smaller number with the same digits.solution').next_smaller

cases = [
    TestCase(1027, -1),
    TestCase(907, 790),
    TestCase(531, 513),
    TestCase(2071, 2017),
    TestCase(414, 144),
    TestCase(123456798, 123456789),
    TestCase(123456789, -1),
    TestCase(1234567908, 1234567890),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_nex_smaller_with_same_digits(self, test):
        assert_true(solution(test.test_data), test.test_output)
