from asserts.asserts import assert_true
import importlib

solve = importlib.import_module('katas.6kyu.Consonant value.solution').solve


class TestSolution:
    def test_consonant_value(self):
        assert_true(solve("zodiac"), 26)
        assert_true(solve("strength"), 57)
