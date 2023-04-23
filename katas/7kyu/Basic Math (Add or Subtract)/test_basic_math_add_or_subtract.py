from asserts.asserts import assert_true
import importlib

calculate = importlib.import_module('katas.7kyu.Basic Math (Add or Subtract).solution').calculate


class TestSolution:
    def test_basic_math_add_or_subtract(self):
        assert_true(calculate('1plus2plus3plus4'), '10')
        assert_true(calculate('1minus2minus3minus4'), '-8')
        assert_true(calculate('1plus2plus3minus4'), '2')
