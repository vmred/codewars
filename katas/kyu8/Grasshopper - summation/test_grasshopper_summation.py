import importlib

from asserts.asserts import assert_true

summation = importlib.import_module('katas.kyu8.Grasshopper - summation.solution').summation


class TestSolution:
    def test_grasshopper_summation(self):
        assert_true(summation(1), 1)
        assert_true(summation(8), 36)
        assert_true(summation(22), 253)
        assert_true(summation(100), 5050)
        assert_true(summation(213), 22791)
