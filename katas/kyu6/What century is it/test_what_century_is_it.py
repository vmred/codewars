from asserts.asserts import assert_true
import importlib

whatCentury = importlib.import_module('katas.kyu6.What century is it.solution').whatCentury


class TestSolution:
    def test_what_century_is_it(self):
        assert_true(whatCentury('1999'), '20th')
        assert_true(whatCentury('2000'), '20th')
        assert_true(whatCentury('1322'), '14th')
