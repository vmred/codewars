import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Where my anagrams at.solution').anagrams

cases = [
    Case(['abba', ['aabb', 'abcd', 'bbaa', 'dada']], ['aabb', 'bbaa']),
    Case(['racer', ['crazer', 'carer', 'racar', 'caers', 'racer']], ['carer', 'racer']),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_where_my_anagrams_at(self, test):
        assert_true(solution(*test.test_data), test.test_output)
