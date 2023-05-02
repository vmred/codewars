import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.flatten().solution').flatten

cases = [
    TestCase([[1], [[8]]], [1, 8]),
    TestCase([[1, 2, 3]], [1, 2, 3]),
    TestCase([1, 2, 3], [1, 2, 3]),
    TestCase([[1, 2], [3, 4, 5], [6, [7], [[8]]]], [1, 2, 3, 4, 5, 6, 7, 8]),
    TestCase([1, 2, ['9', [], []], None], [1, 2, '9', None]),
    TestCase([['hello', 2, ['text', [4, 5]]], [[]], '[list]'], ['hello', 2, 'text', 4, 5, '[list]']),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_flatten_kata(self, test):
        assert_true(solution(*test.test_data), test.test_output)
