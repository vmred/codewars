from functools import reduce


def parts_sums(ls):
    if not ls:
        return [0]

    s = reduce(lambda x, n: x + n, ls)

    sum_arr = [s]

    for i in range(1, len(ls)):
        s -= ls[i - 1]
        sum_arr.append(s)

    sum_arr.append(0)

    return sum_arr