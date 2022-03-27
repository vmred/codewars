import importlib

from asserts.asserts import assert_true

format_duration = importlib.import_module('kyu4.Human readable duration format.solution').format_duration


class TestSolution:
    def test_human_readable_duration_format(self):
        assert_true(format_duration(1), "1 second")
        assert_true(format_duration(62), "1 minute and 2 seconds")
        assert_true(format_duration(120), "2 minutes")
        assert_true(format_duration(3600), "1 hour")
        assert_true(format_duration(3662), "1 hour, 1 minute and 2 seconds")
