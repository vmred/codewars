import importlib

from asserts.Asserts import assert_true

sum_all = importlib.import_module('beta.Sum of all arguments.solution').sum_all


class TestSolution:
    def test_sum_of_all_arguments(self):
        assert_true(sum_all(6, 2, 3), 11)
        assert_true(sum_all(756, 2, 1, 10), 769)
        assert_true(sum_all(76856, -32, 1981, 1076), 79881)
        assert_true(sum_all(1, -32, "codewars", 1076), False)
        assert_true(sum_all(7, -3452, 1981, 1076), -388)
