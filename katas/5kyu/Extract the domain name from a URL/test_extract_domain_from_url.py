import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import TestCase

solution = importlib.import_module('katas.5kyu.Extract the domain name from a URL.solution').domain_name

cases = [
    TestCase("http://google.com", "google"),
    TestCase("http://google.co.jp", "google"),
    TestCase("www.xakep.ru", "xakep"),
    TestCase("https://youtube.com", "youtube"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_extract_domain_from_url(self, test):
        assert_true(solution(test.test_data), test.test_output)
