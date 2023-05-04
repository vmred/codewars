import importlib
from asserts.asserts import assert_true

filter_list = importlib.import_module('katas.7kyu.List filtering.solution').filter_list


class TestSolution:
    def test_list_filtering(self):
        assert_true(filter_list([1, 2, 'a', 'b']), [1, 2])
