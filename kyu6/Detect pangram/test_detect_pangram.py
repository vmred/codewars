from asserts.asserts import assert_true
import importlib

is_pangram = importlib.import_module('kyu6.Detect pangram.solution').is_pangram


class TestSolution:
    def test_pangram(self):
        assert_true(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
        assert_true(is_pangram("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), False)
