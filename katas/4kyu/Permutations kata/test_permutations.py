import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

permutations = importlib.import_module('katas.4kyu.Permutations kata.solution').permutations

cases = [
    Case('ab', ['ab', 'ba']),
    Case('a', ['a']),
    Case('aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_permutations(self, test):
        assert_true(permutations(test.test_data), test.test_output)
