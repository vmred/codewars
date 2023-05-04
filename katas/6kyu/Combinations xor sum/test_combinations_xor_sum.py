import importlib
import pytest

from asserts.asserts import assert_true

from asserts.testcase import TestCase

solution = importlib.import_module('katas.6kyu.Combinations xor sum.solution').transform

cases = [
    TestCase([[7, 4, 11, 6, 5], 3], 384),
    TestCase([[12, 9, 16, 11, 10], 4], 7937),
    TestCase([[9, 6, 13, 9, 7], 2], 375),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_combinations_xor_sum(self, test):
        assert_true(solution(*test.test_data), test.test_output)
