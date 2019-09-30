import re


def sum_of_a_beach(beach):
    return len(re.findall('fish|sand|sun|water', beach.lower()))
