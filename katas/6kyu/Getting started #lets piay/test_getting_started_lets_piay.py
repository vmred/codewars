import importlib
from asserts.asserts import assert_true

whatpimeans = importlib.import_module('katas.6kyu.Getting started #lets piay.solution').whatpimeans


class TestSolution:
    def test_getting_started_lets_piay(self):
        assert_true(whatpimeans(), 'THANKYOU')
