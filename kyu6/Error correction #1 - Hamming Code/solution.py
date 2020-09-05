# kata link - https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/python

from textwrap import wrap

def encode(string):
    return ''.join([bin(ord(x))[2:].zfill(8) for x in string]).replace('0', '000').replace('1', '111')

def decode(bits):
    sp = wrap(bits, 3)
    for i, v in enumerate(sp):
        if v == '111':
            sp[i] = '1'
        elif v == '000':
            sp[i] = '0'
        elif v.count('0') > 1:
            sp[i] = '0'
        else:
            sp[i] = '1'

    sp = int(''.join(sp), 2)

    return sp.to_bytes((sp.bit_length() + 7) // 8, 'big').decode()
