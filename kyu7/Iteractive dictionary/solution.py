# In this kata, your job is to create a class Dictionary which you can add words to and their entries.

# Example:
# >>> d = Dictionary()
# >>> d.newentry('Apple', 'A fruit that grows on trees')

# >>> print(d.look('Apple'))
# A fruit that grows on trees

# >>> print(d.look('Banana'))
# Can't find entry for Banana


class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def newentry(self, word, definition):
        self.dictionary[word] = definition

    def look(self, k):
        return self.dictionary.get(k, 'Can\'t find entry for %s' % k)
