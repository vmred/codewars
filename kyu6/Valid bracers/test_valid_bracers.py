import importlib

from asserts.asserts import assert_true

validBraces = importlib.import_module('kyu6.Valid bracers.solution').validBraces


class TestSolution:
    def test_valid_bracers(self):
        assert_true(validBraces("()"), True)
        assert_true(validBraces("[(])"), False)
