import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Rot13.solution').rot13

cases = [
    Case("test", "grfg"),
    Case("Test", "Grfg"),
    Case('Pbqrjnef', 'Codewars'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_rot13(self, test):
        assert_true(solution(test.test_data), test.test_output)
