from asserts.asserts import assert_true
import importlib

camel_case = importlib.import_module('katas.kyu6.Camel case method.solution').camel_case


class TestSolution:
    def test_camel_case_method(self):
        assert_true(camel_case('test case'), 'TestCase')
