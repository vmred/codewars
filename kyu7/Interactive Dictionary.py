# In this kata, your job is to create a class Dictionary which you can add words to and their entries.

# Example:
# >>> d = Dictionary()
# >>> d.newentry('Apple', 'A fruit that grows on trees')

# >>> print(d.look('Apple'))
# A fruit that grows on trees

# >>> print(d.look('Banana'))
# Can't find entry for Banana
from asserts.Asserts import assert_true


class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def newentry(self, word, definition):
        self.dictionary[word] = definition

    def look(self, k):
        return self.dictionary.get(k, 'Can\'t find entry for %s' % k)


d = Dictionary()

d.newentry("Apple", "A fruit")
assert_true(d.look("Apple"), "A fruit")

d.newentry("Soccer", "A sport")
assert_true(d.look("Soccer"), "A sport")
assert_true(d.look("Hi"), "Can't find entry for Hi")
assert_true(d.look("Ball"), "Can't find entry for Ball")
