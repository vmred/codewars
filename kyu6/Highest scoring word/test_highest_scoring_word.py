from asserts.asserts import assert_true
import importlib

high = importlib.import_module('kyu6.Highest scoring word.solution').high


class TestSolution:
    def test_highest_scoring_word(self):
        assert_true(high('man i need a taxi up to ubud'), 'taxi')
