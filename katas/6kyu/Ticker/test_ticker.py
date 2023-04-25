from asserts.asserts import assert_true
import importlib

ticker = importlib.import_module('katas.6kyu.Ticker.solution').ticker


class TestSolution:
    def test_ticker(self):
        assert_true(ticker('Beautiful is better than ugly.', 10, 0), '          ')
        assert_true(ticker('Beautiful is better than ugly.', 10, 1), '         B')
        assert_true(ticker('Beautiful is better than ugly.', 10, 5), '     Beaut')
        assert_true(ticker('Beautiful is better than ugly.', 10, 30), 'than ugly.')
        assert_true(ticker('Beautiful is better than ugly.', 10, 39), '.         ')
        assert_true(ticker('Beautiful is better than ugly.', 10, 41), '         B')
        assert_true(ticker('Foobar', 10, 19), '       Foo')
        assert_true(ticker('such now time be?', 1, 4651), 'o')
