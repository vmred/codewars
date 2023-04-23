# Given a time in AM/PM format as a string, convert it to military (24-hour) time as a string.

# Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
# Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock

# Sample Input: 07:05:45PM Sample Output: 19:05:45
# Try not to use built in DateTime libraries.

# For more information on military time, check the wiki https://en.wikipedia.org/wiki/24-hour_clock


def get_military_time(time):
    if 'AM' in time:
        time = time.replace('AM', '')
        if time.startswith('12'):
            time = time.replace('12', '00')

    if 'PM' in time:
        time = time.replace('PM', '')
        hour = time[:2]
        if hour != '12':
            time = time.replace(hour, str(int(hour) + 12))

    return time
