# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
import math

from asserts.Asserts import assert_true


def make_readable(seconds):
    hours = math.floor(seconds / 3600)
    seconds -= hours * 3600
    if hours < 10:
        hours = '0{}'.format(hours)

    minutes = math.floor(seconds / 60)
    seconds -= minutes * 60
    if minutes < 10:
        minutes = '0{}'.format(minutes)

    if seconds < 10:
        seconds = '0{}'.format(seconds)

    return '{}:{}:{}'.format(hours, minutes, seconds)

    # one line solution
    # return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)


class TestSolution:
    def test_solution(self):
        assert_true(make_readable(0), "00:00:00")
        assert_true(make_readable(86399), "23:59:59")
        assert_true(make_readable(359999), "99:59:59")
