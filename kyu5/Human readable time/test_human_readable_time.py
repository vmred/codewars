from asserts.Asserts import assert_true
import importlib

make_readable = importlib.import_module('kyu5.Human readable time.solution').make_readable


class TestSolution:

    def test_human_readable_time(self):
        assert_true(make_readable(0), "00:00:00")
        assert_true(make_readable(86399), "23:59:59")
        assert_true(make_readable(359999), "99:59:59")
