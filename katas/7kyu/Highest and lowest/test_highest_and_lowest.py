import importlib
from asserts.asserts import assert_true

high_and_low = importlib.import_module('katas.7kyu.Highest and lowest.solution').high_and_low


class TestSolution:
    def test_highest_and_lowest(self):
        assert_true(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214")
