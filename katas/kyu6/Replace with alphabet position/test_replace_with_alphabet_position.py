from asserts.asserts import assert_true
import importlib

alphabet_position = importlib.import_module('katas.kyu6.Replace with alphabet position.solution').alphabet_position


class TestSolution:
    def test_replace_with_alphabet_position(self):
        assert_true(alphabet_position("The narwhal bacons at midnight."),
                    "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
