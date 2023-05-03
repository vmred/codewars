# Human readable time
# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
import math


def make_readable(seconds):
    hours = math.floor(seconds / 3600)
    seconds -= hours * 3600
    if hours < 10:
        hours = f'0{hours}'

    minutes = math.floor(seconds / 60)
    seconds -= minutes * 60
    if minutes < 10:
        minutes = f'0{minutes}'

    if seconds < 10:
        seconds = f'0{seconds}'

    return f'{hours}:{minutes}:{seconds}'

    # one line solution
    # return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
