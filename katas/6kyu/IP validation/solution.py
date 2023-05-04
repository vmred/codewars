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


def is_valid_IP(s):
    ip = s.split('.')

    if len(ip) != 4:
        return False

    for i in ip:
        if ' ' in i or i.isalpha() or not 0 < len(i) < 4 or not 0 < int(i) < 256 or i[0] == '0':
            return False

    return True

    # return s.count('.') == 3 and all(o.isdigit() and 0 <= int(o) <= 255 and str(int(o)) == o for o in s.split('.'))
