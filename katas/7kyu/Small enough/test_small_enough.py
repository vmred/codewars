import importlib
from asserts.asserts import assert_true

small_enough = importlib.import_module('katas.7kyu.Small enough.solution').small_enough


class TestSolution:
    def test_small_enough(self):
        assert_true(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100), False)
