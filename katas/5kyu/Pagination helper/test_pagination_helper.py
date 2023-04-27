import pytest

from asserts.asserts import assert_true
import importlib

from asserts.testcase import TestCase

PaginationHelper = importlib.import_module('katas.5kyu.Pagination helper.solution').PaginationHelper

helper = PaginationHelper(range(1, 25), 10)

cases = [
    TestCase('no args', 3, test_function=helper.page_count),
    TestCase(23, 2, test_function=helper.page_index),
    TestCase('no args', 24, test_function=helper.item_count),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_remove_the_parentheses(self, test):
        assert_true(
            test.test_data != 'no args' and test.test_function(test.test_data) or test.test_function(), test.test_output
        )
