from asserts.asserts import assert_true
import importlib

filter_list = importlib.import_module('katas.kyu7.List filtering.solution').filter_list


class TestSolution:
    def test_list_filtering(self):
        assert_true(filter_list([1, 2, 'a', 'b']), [1, 2])
