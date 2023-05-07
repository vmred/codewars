import importlib

import pytest

from asserts.asserts import assert_true
from asserts.testcase import Case

Dinglemouse = importlib.import_module('katas.6kyu.FIXME Hello.solution').Dinglemouse

cases = [
    Case(Dinglemouse().setName("Bob").setAge(27).setSex('M'), "Hello. My name is Bob. I am 27. I am male."),
    Case(Dinglemouse().setName("Batman"), "Hello. My name is Batman."),
    Case(Dinglemouse().setAge(27).setSex('M').setName("Bob"), "Hello. I am 27. I am male. My name is Bob."),
]


class TestSolution:
    @pytest.mark.parametrize('test', cases, ids=[f'{test.test_data}' for test in cases])
    def test_fixme_hello(self, test):
        assert_true(test.test_data.hello(), test.test_output)
