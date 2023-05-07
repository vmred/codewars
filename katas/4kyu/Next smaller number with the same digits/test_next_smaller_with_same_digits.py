import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.4kyu.Next smaller number with the same digits.solution').next_smaller

cases = [
    Case(1027, -1),
    Case(907, 790),
    Case(531, 513),
    Case(2071, 2017),
    Case(414, 144),
    Case(123456798, 123456789),
    Case(123456789, -1),
    Case(1234567908, 1234567890),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_nex_smaller_with_same_digits(self, test):
        assert_true(solution(test.test_data), test.test_output)
