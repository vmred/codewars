import importlib
from asserts.asserts import assert_true

disarium_number = importlib.import_module('katas.7kyu.Disarium number.solution').disarium_number


class TestSolution:
    def test_disarium_number(self):
        assert_true(disarium_number(89), "Disarium !!")
        assert_true(disarium_number(518), "Disarium !!")
        assert_true(disarium_number(1024), "Not !!")
