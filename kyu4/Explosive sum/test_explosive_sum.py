import importlib

from asserts.Asserts import assert_true

exp_sum = importlib.import_module('kyu4.Explosive sum.solution').exp_sum


class TestSolution:
    def test_exposive_sum(self):
        assert_true(exp_sum(1), 1)
        assert_true(exp_sum(2), 2)
        assert_true(exp_sum(3), 3)

        assert_true(exp_sum(4), 5)
        assert_true(exp_sum(5), 7)
        assert_true(exp_sum(10), 42)
