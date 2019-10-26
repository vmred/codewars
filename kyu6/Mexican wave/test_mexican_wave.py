from asserts.Asserts import assert_true
import importlib

wave = importlib.import_module('kyu6.Mexican wave.solution').wave


class TestSolution:
    def test_mexican_wave(self):
        assert_true(wave("hello"), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
        assert_true(wave("codewars"),
                    ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"])
        assert_true(wave(""), [])
        assert_true(wave("two words"),
                    ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs",
                     "two wordS"])
        assert_true(wave(" gap "), [" Gap ", " gAp ", " gaP "])
