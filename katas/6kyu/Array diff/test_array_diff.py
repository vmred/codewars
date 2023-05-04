import importlib
import pytest
from asserts.asserts import assert_true
from asserts.test_case import TestCase


solution = importlib.import_module('katas.6kyu.Array diff.solution').array_diff


class TestSolution:
    def test_array_diff(self):
        assert_true(array_diff([1, 2], [1]), [2])
        assert_true(array_diff([1, 2, 2], []), [1, 2, 2])

cases = [
    TestCase([[1, 2], [1]], [2]),
    TestCase([[1, 2, 2], []], [1, 2, 2]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_array_diff(self, test):
        assert_true(solution(*test.test_data), test.test_output)
