# A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet,
# where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.

# E.g.
# map1 = 'abcdefghijklmnopqrstuvwxyz';
# map2 = 'etaoinshrdlucmfwypvbgkjqxz';

# cipher = Cipher(map1, map2);
# cipher.encode('abc') # => 'eta'
# cipher.encode('xyz') # => 'qxz'
# cipher.encode('aeiou') # => 'eirfg'

# cipher.decode('eta') # => 'abc'
# cipher.decode('qxz') # => 'xyz'
# cipher.decode('eirfg') # => 'aeiou'
from asserts.Asserts import assert_true


class Cipher(object):
    def __init__(self, m1, m2):
        self.decode_map = list(m1)
        self.encode_map = list(m2)

    def encode(self, string):
        return ''.join([self.encode_map[self.decode_map.index(i)] if i in self.encode_map else i for i in string])

    def decode(self, string):
        return ''.join([self.decode_map[self.encode_map.index(i)] if i in self.decode_map else i for i in string])


map1 = 'abcdefghijklmnopqrstuvwxyz'
map2 = 'etaoinshrdlucmfwypvbgkjqxz'

cipher = Cipher(map1, map2)
assert_true(cipher.encode('a_bc&*83'), 'e_ta&*83')
assert_true(cipher.encode('abc'), 'eta')
assert_true(cipher.encode('xyz'), 'qxz')
assert_true(cipher.decode('eirfg'), 'aeiou')
assert_true(cipher.decode('erlang'), 'aikcfu')

map2 = 'tfozcivbsjhengarudlkpwqxmy'
cipher = Cipher(map1, map2)
assert_true(cipher.encode('abc'), 'tfo')
assert_true(cipher.decode('tfo'), 'abc')
assert_true(cipher.decode('kjpphi'), 'tjuukf')
assert_true(cipher.encode('ajqqtb'), 'tjuukf')
