from asserts.Asserts import assert_true
import importlib

minimum_steps = importlib.import_module('kyu7.Minimum steps.solution').minimum_steps


class TestSolution:
    def test_minimum_steps(self):
        assert_true(minimum_steps([4, 6, 3], 7), 1)
        assert_true(minimum_steps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464), 8)
