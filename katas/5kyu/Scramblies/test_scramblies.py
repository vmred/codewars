import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Scramblies.solution').scramble

cases = [
    Case(['rkqodlw', 'world'], True),
    Case(['cedewaraaossoqqyt', 'codewars'], True),
    Case(['katas', 'steak'], False),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_scramblies(self, test):
        assert_true(solution(*test.test_data), test.test_output)
