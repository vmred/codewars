from asserts.Asserts import assert_true
import importlib

randint = importlib.import_module('kyu6.Dont rely on luck.solution').randint
guess = importlib.import_module('kyu6.Dont rely on luck.solution').guess


class TestSolution:
    def test_dont_rely_on_luck(self):
        lucky_number = randint(1, 100)
        assert_true(guess, lucky_number)
