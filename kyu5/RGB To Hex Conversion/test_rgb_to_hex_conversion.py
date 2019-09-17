import importlib

from asserts.Asserts import assert_true

rgb = importlib.import_module('kyu5.RGB To Hex Conversion.solution').rgb


class TestSolution:
    def test_rgb_to_hex_conversion(self):
        assert_true(rgb(0, 0, 0), "000000")
        assert_true(rgb(1, 2, 3), "010203")
        assert_true(rgb(255, 255, 255), "FFFFFF")
        assert_true(rgb(254, 253, 252), "FEFDFC")
        assert_true(rgb(-20, 275, 125), "00FF7D")
