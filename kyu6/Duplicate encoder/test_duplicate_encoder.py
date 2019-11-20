from asserts.Asserts import assert_true
import importlib

duplicate_encode = importlib.import_module('kyu6.Duplicate encoder.solution').duplicate_encode


class TestSolution:
    def test_duplicate_encoder(self):
        assert_true(duplicate_encode('recede'), '()()()')
        assert_true(duplicate_encode('Supralapsarian'), ')()))()))))()(')
