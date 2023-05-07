import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Delete occurrences of element.solution').delete_nth

cases = [
    Case([[20, 37, 20, 21], 1], [20, 37, 21]),
    Case([[1, 1, 3, 3, 7, 2, 2, 2, 2], 3], [1, 1, 3, 3, 7, 2, 2, 2]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_delete_occurrences_of_element(self, test):
        assert_true(solution(*test.test_data), test.test_output)
