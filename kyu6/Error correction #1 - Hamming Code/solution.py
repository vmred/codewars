# kata link - https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e/python

from textwrap import wrap

def encode(string):
    return ''.join([bin(ord(x))[2:].zfill(8) for x in string]).replace('0', '000').replace('1', '111')

def decode(bits):
    bits = int(''.join(''.join(['1' if x.count('1') > x.count('0') else '0' for x in wrap(bits, 3)])), 2)
    return bits.to_bytes((bits.bit_length() + 7) // 8, 'big').decode()
