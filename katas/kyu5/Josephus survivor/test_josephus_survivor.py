from asserts.asserts import assert_true
import importlib

josephus_survivor = importlib.import_module('katas.kyu5.Josephus survivor.solution').josephus_survivor


class TestSolution:
    def test_josephus_survivor(self):
        assert_true(josephus_survivor(7, 3), 4)
        assert_true(josephus_survivor(11, 19), 10)
        assert_true(josephus_survivor(1, 300), 1)
        assert_true(josephus_survivor(14, 2), 13)
        assert_true(josephus_survivor(100, 1), 100)
