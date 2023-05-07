import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Function Composition.solution').compose

cases = [
    Case([lambda a: a + 1, lambda a: a], 1),  # TODO pylint: disable=fixme
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_function_composition(self, test):
        assert_true(solution(*test.test_data)(0), test.test_output)
