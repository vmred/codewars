from asserts.asserts import assert_true
import importlib

max_tri_sum = importlib.import_module('kyu7.Maximum triplet sum.solution').max_tri_sum


class TestSolution:
    def test_maximum_triplet_sum(self):
        assert_true(max_tri_sum([3, 2, 6, 8, 2, 3]), 17)
        assert_true(max_tri_sum([2, 9, 13, 10, 5, 2, 9, 5]), 32)
