import importlib

order_by_domain = importlib.import_module('kyu6.com gov org first.solution').order_by_domain


class TestSolution:
    def test_com_gov_org_first(self, test_case):
        test_case.verify(order_by_domain([
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
