import importlib
from asserts.asserts import assert_true

nth_smallest = importlib.import_module('katas.7kyu.Nth smallest element.solution').nth_smallest


class TestSolution:
    def test_nth_smallest_element(self):
        assert_true(nth_smallest([3, 1, 2], 2), 2)
