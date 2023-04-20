import importlib

from asserts.asserts import assert_true

domain_name = importlib.import_module('katas.kyu5.Extract the domain name from a URL.solution').domain_name


class TestSolution:
    def test_extract_domain_from_url(self):
        assert_true(domain_name("http://google.com"), "google")
        assert_true(domain_name("http://google.co.jp"), "google")
        assert_true(domain_name("www.xakep.ru"), "xakep")
        assert_true(domain_name("https://youtube.com"), "youtube")
