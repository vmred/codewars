import importlib
from asserts.asserts import assert_true

unique_in_order = importlib.import_module('katas.6kyu.Unique in order.solution').unique_in_order


class TestSolution:
    def test_unique_in_order(self):
        assert_true(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
        assert_true(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])
        assert_true(unique_in_order('A'), ['A'])
        assert_true(unique_in_order('AA'), ['A'])
        assert_true(unique_in_order(''), [])
