from asserts.asserts import assert_true
import importlib

Dinglemouse = importlib.import_module('katas.kyu6.FIXME Hello.solution').Dinglemouse


class TestSolution:
    def test_fixme_hello(self):
        dm = Dinglemouse().setName("Bob").setAge(27).setSex('M')
        expected = "Hello. My name is Bob. I am 27. I am male."
        assert_true(dm.hello(), expected)

        dm = Dinglemouse().setName("Batman")
        expected = "Hello. My name is Batman."
        assert_true(dm.hello(), expected)

        dm = Dinglemouse().setAge(27).setSex('M').setName("Bob")
        expected = "Hello. I am 27. I am male. My name is Bob."
        assert_true(dm.hello(), expected)
