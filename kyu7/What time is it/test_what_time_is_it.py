from asserts.Asserts import assert_true
import importlib

get_military_time = importlib.import_module('kyu7.What time is it.solution').get_military_time


class TestSolution:
    def test_what_time_is_it(self):
        assert_true(get_military_time('12:00:01AM'), '00:00:01')
        assert_true(get_military_time('11:46:47PM'), '23:46:47')
        assert_true(get_military_time('12:24:25PM'), '12:24:25')
