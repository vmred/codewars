import importlib
from asserts.asserts import assert_true

high = importlib.import_module('katas.6kyu.Highest scoring word.solution').high


class TestSolution:
    def test_highest_scoring_word(self):
        assert_true(high('man i need a taxi up to ubud'), 'taxi')
