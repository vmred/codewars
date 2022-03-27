from asserts.asserts import assert_true
import importlib

whatpimeans = importlib.import_module('kyu6.Getting started #lets piay.solution').whatpimeans


class TestSolution:
    def test_getting_started_lets_piay(self):
        assert_true(whatpimeans(), 'THANKYOU')
