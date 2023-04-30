import pytest

from asserts.asserts import assert_true
import importlib

PaginationHelper = importlib.import_module('katas.5kyu.Pagination helper.solution').PaginationHelper


class TestSolution:
    @pytest.mark.xfail
    @pytest.mark.not_competed
    def test_pagination_helper(self):
        collection = range(1, 25)
        helper = PaginationHelper(collection, 10)

        assert_true(helper.page_count(), 3)
        assert_true(helper.page_index(23), 2)
        assert_true(helper.item_count(), 24)
