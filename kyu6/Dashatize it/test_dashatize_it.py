from asserts.Asserts import assert_true
import importlib

dashatize = importlib.import_module('kyu6.Dashatize it.solution').dashatize


class TestSolution:
    def test_dashatize_it(self):
        assert_true(dashatize(274), "2-7-4")
        assert_true(dashatize(86320), "86-3-20")
        assert_true(dashatize(-1), "1")
        assert_true(dashatize(0), "0")
        assert_true(dashatize(None), 'None')
