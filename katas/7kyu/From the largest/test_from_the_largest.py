import importlib
from asserts.asserts import assert_true

max_number = importlib.import_module('katas.7kyu.From the largest.solution').max_number


class TestSolution:
    def test_from_the_largest(self):
        assert_true(max_number(213), 321)
