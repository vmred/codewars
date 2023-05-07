import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Pyramid array.solution').pyramid

cases = [Case(0, []), Case(1, [[1]]), Case(2, [[1], [1, 1]]), Case(3, [[1], [1, 1], [1, 1, 1]])]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_pyramid_array(self, test):
        assert_true(solution(test.test_data), test.test_output)
