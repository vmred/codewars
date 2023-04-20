from asserts.asserts import assert_true
import importlib

small_enough = importlib.import_module('katas.kyu7.Small enough.solution').small_enough


class TestSolution:
    def test_small_enough(self):
        assert_true(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100), False)
