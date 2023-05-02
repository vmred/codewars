import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.4kyu.Next bigger number with the same digits.solution').next_bigger

cases = [
    TestCase(12, 21),
    TestCase(513, 531),
    TestCase(2017, 2071),
    TestCase(414, 441),
    TestCase(144, 414),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_nex_bigger_with_same_digits(self, test):
        assert_true(solution(test.test_data), test.test_output)
