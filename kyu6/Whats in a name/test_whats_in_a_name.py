from asserts.Asserts import assert_true
import importlib

name_in_str = importlib.import_module('kyu6.Whats in a name.solution').name_in_str


class TestSolution:
    def test_whats_in_a_name(self):
        assert_true(name_in_str("Across the rivers", "chris"), True)
        assert_true(name_in_str("A crew that boards the ship", "chris"), False)
        assert_true(name_in_str("Next to a lake", "chris"), False)
