import importlib
from asserts.asserts import assert_true

is_nice = importlib.import_module('katas.7kyu.Nice array.solution').is_nice


class TestSolution:
    def test_nice_array(self):
        assert_true(is_nice([2, 10, 9, 3]), True)
        assert_true(is_nice([3, 4, 5, 7]), False)
