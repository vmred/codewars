import importlib
from asserts.asserts import assert_true

printer_error = importlib.import_module('katas.7kyu.Printer errors.solution').printer_error


class TestSolution:
    def test_printer_errors(self):
        assert_true(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "3/56")
        assert_true(printer_error("aaaxbbbbyyhwawiwjjjwwm"), '8/22')
