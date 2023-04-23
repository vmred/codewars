from asserts.asserts import assert_true
import importlib

camel_case = importlib.import_module('katas.6kyu.Camel case method.solution').camel_case


class TestSolution:
    def test_camel_case_method(self):
        assert_true(camel_case('test case'), 'TestCase')
