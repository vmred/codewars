from asserts.Asserts import assert_true
import importlib

to_camel_case = importlib.import_module('kyu6.Convert string to camel case.solution').to_camel_case


class TestSolution:
    def test_convert_string_to_camel_case(self):
        assert_true(to_camel_case("the_stealth_warrior"), "theStealthWarrior")
