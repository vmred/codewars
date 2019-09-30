from asserts.Asserts import assert_true
import importlib

unlucky_days = importlib.import_module('kyu7.Unlucky days.solution').unlucky_days


class TestSolution:
    def test_unlucky_days(self):
        assert_true(unlucky_days(2015), 3)
        assert_true(unlucky_days(1986), 1)
