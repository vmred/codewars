import importlib
from asserts.asserts import assert_true

longest = importlib.import_module('katas.7kyu.Two to one.solution').longest


class TestSolution:
    def test_two_to_one(self):
        assert_true(longest("aretheyhere", "yestheyarehere"), "aehrsty")
