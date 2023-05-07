import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

solution = importlib.import_module('katas.5kyu.Extract the domain name from a URL.solution').domain_name

cases = [
    Case("http://google.com", "google"),
    Case("http://google.co.jp", "google"),
    Case("www.xakep.ru", "xakep"),
    Case("https://youtube.com", "youtube"),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_extract_domain_from_url(self, test):
        assert_true(solution(test.test_data), test.test_output)
