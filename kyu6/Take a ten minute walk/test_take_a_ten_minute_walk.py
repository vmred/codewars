from asserts.Asserts import assert_true
import importlib

isValidWalk = importlib.import_module('kyu6.Take a ten minute walk.solution').isValidWalk


class TestSolution:
    def test_take_a_ten_minute_walk(self):
        assert_true(isValidWalk('nws'), False)
