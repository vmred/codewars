import importlib
import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.6kyu.Numericals of a String.solution').numericals

cases = [
    Case('Hello, World!', '1112111121311'),
    Case("Hello, World! It's me, JomoPipi!", '11121111213112111131224132411122'),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_numericals_of_a_string(self, test):
        assert_true(solution(test.test_data), test.test_output)
