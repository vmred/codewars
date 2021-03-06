import importlib

from asserts.Asserts import assert_true

expanded_form = importlib.import_module('kyu6.Write Number in Expanded Form.solution').expanded_form


class TestSolution:
    def test_write_number_in_expanded_form(self):
        assert_true(expanded_form(12), '10 + 2')
        assert_true(expanded_form(42), '40 + 2')
        assert_true(expanded_form(70304), '70000 + 300 + 4')
