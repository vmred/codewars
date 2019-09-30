from asserts.Asserts import assert_true
import importlib

disarium_number = importlib.import_module('kyu7.Disarium number.solution').disarium_number


class TestSolution:
    def test_disarium_number(self):
        assert_true(disarium_number(89), "Disarium !!")
        assert_true(disarium_number(518), "Disarium !!")
        assert_true(disarium_number(1024), "Not !!")
