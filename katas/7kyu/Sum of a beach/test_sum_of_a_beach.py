import importlib
from asserts.asserts import assert_true

sum_of_a_beach = importlib.import_module('katas.7kyu.Sum of a beach.solution').sum_of_a_beach


class TestSolution:
    def test_sum_of_beach(self):
        assert_true(sum_of_a_beach("sunsunsunsun"), 4)
