from asserts.Asserts import assert_true
import importlib

count = importlib.import_module('kyu6.Count characters in your string.solution').count


class TestSolution:
    def test_count_characters_in_your_string(self):
        assert_true(count('aba'), {'a': 2, 'b': 1})

