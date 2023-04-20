from asserts.asserts import assert_true
import importlib

find_missing_number = importlib.import_module('katas.kyu6.Number Zoo Patrol.solution').find_missing_number


class TestSolution:
    def test_number_zoo_patrol(self):
        assert_true(find_missing_number([2, 3, 4]), 1)
        assert_true(find_missing_number([1, 2, 3]), 4)
        assert_true(find_missing_number([1, 2, 4]), 3)
