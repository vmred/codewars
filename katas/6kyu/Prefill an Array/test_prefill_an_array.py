import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Prefill an Array.solution').prefill

cases = [Case([3, 1], [1, 1, 1]), Case([2, 'abc'], ['abc', 'abc'])]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_prefill_an_array(self, test):
        assert_true(solution(*test.test_data), test.test_output)
