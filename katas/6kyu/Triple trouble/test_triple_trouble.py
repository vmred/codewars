import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Triple trouble.solution').triple_double

cases = [
    Case([451999277, 41177722899], 1),
    Case([1112, 122], 0),
    Case([10560002, 100], 1),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def triple_double(self, test):
        assert_true(solution(*test.test_data), test.test_output)
