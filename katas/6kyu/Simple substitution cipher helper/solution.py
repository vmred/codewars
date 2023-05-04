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


class Cipher:
    def __init__(self, m1, m2):
        self.decode_map = list(m1)
        self.encode_map = list(m2)

    def encode(self, string):
        return ''.join([self.encode_map[self.decode_map.index(i)] if i in self.encode_map else i for i in string])

    def decode(self, string):
        return ''.join([self.decode_map[self.encode_map.index(i)] if i in self.decode_map else i for i in string])
