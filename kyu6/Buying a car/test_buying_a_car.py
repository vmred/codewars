from asserts.Asserts import assert_true
import importlib

nbMonths = importlib.import_module('kyu6.Buying a car.solution').nbMonths


class TestSolution:
    def test_buying_a_car(self):
        assert_true(nbMonths(2000, 8000, 1000, 1.5), [6, 766])
        assert_true(nbMonths(12000, 8000, 1000, 1.5), [0, 4000])
