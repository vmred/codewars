from asserts.Asserts import assert_true
import importlib

longest = importlib.import_module('kyu7.Two to one.solution').longest


class TestSolution:
    def test_two_to_one(self):
        assert_true(longest("aretheyhere", "yestheyarehere"), "aehrsty")
