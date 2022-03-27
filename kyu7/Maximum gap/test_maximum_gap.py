from asserts.asserts import assert_true
import importlib

max_gap = importlib.import_module('kyu7.Maximum gap.solution').max_gap


class TestSolution:
    def test_maximum_gap(self):
        assert_true(max_gap([13, 10, 2, 9, 5]), 4)
