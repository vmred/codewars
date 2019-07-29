import re
from asserts.Asserts import assert_true


def sum_of_a_beach(beach):
    return len(re.findall('fish|sand|sun|water', beach.lower()))


assert_true(sum_of_a_beach("sunsunsunsun"), 4)
