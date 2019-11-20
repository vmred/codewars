from asserts.Asserts import assert_true
import importlib

goodVsEvil = importlib.import_module('kyu6.Good vs Evil.solution').goodVsEvil


class TestSolution:
    def test_good_vs_evil(self):
        assert_true(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'), 'Battle Result: Evil eradicates all trace of Good')
        assert_true(goodVsEvil('441 856 420 152 146 622', '823 86 367 77 464 304 551'),
                    'Battle Result: Good triumphs over Evil')
