from asserts.asserts import assert_true
import importlib

is_nice = importlib.import_module('katas.kyu7.Nice array.solution').is_nice


class TestSolution:
    def test_nice_array(self):
        assert_true(is_nice([2, 10, 9, 3]), True)
        assert_true(is_nice([3, 4, 5, 7]), False)
