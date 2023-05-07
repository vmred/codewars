import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.4kyu.Next bigger number with the same digits.solution').next_bigger

cases = [
    Case(12, 21),
    Case(513, 531),
    Case(2017, 2071),
    Case(414, 441),
    Case(144, 414),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_nex_bigger_with_same_digits(self, test):
        assert_true(solution(test.test_data), test.test_output)
