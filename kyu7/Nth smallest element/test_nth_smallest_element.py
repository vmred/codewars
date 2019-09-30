from asserts.Asserts import assert_true
import importlib

nth_smallest = importlib.import_module('kyu7.Nth smallest element.solution').nth_smallest


class TestSolution:
    def test_nth_smallest_element(self):
        assert_true(nth_smallest([3, 1, 2], 2), 2)
