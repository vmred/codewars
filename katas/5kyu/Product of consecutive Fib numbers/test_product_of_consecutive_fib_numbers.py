import importlib
import pytest
from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Product of consecutive Fib numbers.solution').productFib

cases = [
    Case(4895, [55, 89, True]),
    Case(5895, [89, 144, False]),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_product_of_consecutive_fib_numbers(self, test):
        assert_true(solution(test.test_data), test.test_output)
