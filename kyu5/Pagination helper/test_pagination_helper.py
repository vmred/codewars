from asserts.asserts import assert_true
import importlib

PaginationHelper = importlib.import_module('kyu5.Pagination helper.solution').PaginationHelper


class TestSolution:

    def test_pagination_helper(self):
        collection = range(1, 25)
        helper = PaginationHelper(collection, 10)

        assert_true(helper.page_count(), 3)
        assert_true(helper.page_index(23), 2)
        assert_true(helper.item_count(), 24)
