import importlib
from asserts.asserts import assert_true

max_gap = importlib.import_module('katas.7kyu.Maximum gap.solution').max_gap


class TestSolution:
    def test_maximum_gap(self):
        assert_true(max_gap([13, 10, 2, 9, 5]), 4)
