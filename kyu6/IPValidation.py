# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Input to the function is guaranteed to be a single string.

# Examples
# Valid inputs:
# 1.2.3.4
# 123.45.67.89

# Invalid inputs:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
from asserts.Asserts import assert_true


def is_valid_IP(strng):
    ip = strng.split('.')

    if len(ip) != 4:
        return False

    for i in ip:
        if ' ' in i:
            return False

        if i.isalpha():
            return False

        if not 0 < len(i) < 4:
            return False

        if not 0 < int(i) < 256:
            return False

        if i[0] == '0':
            return False

    return True

    # return s.count('.') == 3 and all(o.isdigit() and 0 <= int(o) <= 255 and str(int(o)) == o for o in s.split('.'))


assert_true(is_valid_IP('12.255.56.1'), True)
assert_true(is_valid_IP(''), False)
assert_true(is_valid_IP('abc.def.ghi.jkl'), False)
assert_true(is_valid_IP('12.34.56 .1'), False)
