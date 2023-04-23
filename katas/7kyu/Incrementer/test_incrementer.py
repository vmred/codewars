from asserts.asserts import assert_true
import importlib

incrementer = importlib.import_module('katas.7kyu.Incrementer.solution').incrementer


class TestSolution:
    def test_increment(self):
        assert_true(incrementer([1, 2, 3]), [2, 4, 6])
        assert_true(incrementer([3, 6, 9, 8, 9]), [4, 8, 2, 2, 4])
