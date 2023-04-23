# You have to create a function that takes a positive integer number
# and returns the next bigger number formed by the same digits:
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071

# If no bigger number can be composed using those digits, return -1:
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1


def next_bigger(num):
    digits = [int(i) for i in str(num)]
    idx = len(digits) - 1
    while idx >= 1 and digits[idx - 1] >= digits[idx]:
        idx -= 1
    if idx == 0:
        return -1
    pivot = digits[idx - 1]
    swap_idx = len(digits) - 1
    while pivot >= digits[swap_idx]:
        swap_idx -= 1
    digits[swap_idx], digits[idx - 1] = digits[idx - 1], digits[swap_idx]
    digits[idx:] = digits[:idx - 1:-1]
    return int(''.join(str(x) for x in digits))
