import importlib
from asserts.asserts import assert_true

unlucky_days = importlib.import_module('katas.7kyu.Unlucky days.solution').unlucky_days


class TestSolution:
    def test_unlucky_days(self):
        assert_true(unlucky_days(2015), 3)
        assert_true(unlucky_days(1986), 1)
