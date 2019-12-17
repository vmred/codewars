from asserts.Asserts import assert_true
import importlib

parse = importlib.import_module('kyu6.Make the Deadfish swim.solution').parse


class TestSolution:
    def test_make_the_deadfish_swim(self):
        assert_true(parse("ooo"), [0, 0, 0])
        assert_true(parse("ioioio"), [1, 2, 3])
        assert_true(parse("isoisoiso"), [1, 4, 25])
