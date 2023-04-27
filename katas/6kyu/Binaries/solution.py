# Let us take a string composed of decimal digits: "10111213".
# We want to code this string as a string of 0 and 1 and after that be able to decode it.

# We decompose the given string in its decimal numbers 1 0 1 1 1 2 1 3 and we will code each decimal number.

# Coding process to code a number n expressed in base 10:
# a) Let k be the number of bits of n
# b) Put k-1 0 followed by a 1
# c) Put number n in binary
# d) Concat the result of b) and c)

# So we code 0 as 10, 1 as 11 ... etc...

# Repeating this process with the initial string

# "10111213" becomes : "11101111110110110111" resulting of concatenation of 11 10 11 11 11 0110 11 0111 .

# Task:
# Given strng a string of digits representing a decimal number the function code(strng)
# should return the coding of strng as explained above.

# Given a string strng resulting from the previous coding, decode it to get the corresponding decimal string.


def code(strng):
    nums = [int(i) for i in strng]
    return ''.join(['0' * (i.bit_length() - 1) + '1' + '{0:b}'.format(i) for i in nums])


def decode(strng):
    strng = list(strng)
    r = []

    # getting stripped values of step a and b
    while len(strng) > 0:
        index_one = strng.index('1')
        s = len(strng[: index_one + 1]) + 1
        v = strng[: index_one + s]

        l_v = len(v)
        l_v = int(l_v / 2)
        r.append((''.join(v[:l_v]), ''.join(v[l_v:])))

        strng = strng[index_one + s :]

    return ''.join([str(int(i[1], 2)) for i in r])
