from asserts.asserts import assert_true
import importlib

bool_to_word = importlib.import_module('kyu8.Convert boolean values to strings \'Yes\' or \'No\'.solution').bool_to_word


class TestSolution:
    def test_convert_boolean_values_to_strings_yes_or_no(self):
        assert_true(bool_to_word(True), 'Yes')
