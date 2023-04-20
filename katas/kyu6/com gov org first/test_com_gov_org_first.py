import importlib

from asserts.asserts import assert_true

order_by_domain = importlib.import_module('katas.kyu6.com gov org first.solution').order_by_domain


class TestSolution:
    def test_com_gov_org_first(self):
        assert_true(order_by_domain([
            "http://www.google.en/?x=jsdfkj",
            "http://www.google.de/?x=jsdfkj",
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.org/?x=jsdfkj",
            "http://www.google.gov/?x=jsdfkj",
        ]), [
            "http://www.google.com/?x=jsdfkj",
            "http://www.google.gov/?x=jsdfkj",
            "http://www.google.org/?x=jsdfkj",
            "http://www.google.de/?x=jsdfkj",
            "http://www.google.en/?x=jsdfkj",
        ])
