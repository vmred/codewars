import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Length of missing array.solution').get_length_of_missing_array

cases = [Case([[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]], 3), Case([[None, [1, 2]]], 0)]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_length_of_missing_array(self, test):
        assert_true(solution(*test.test_data), test.test_output)
