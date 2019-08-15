# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.

# Implement a function likes :: [String] -> String, which must take in input array,
# containing the names of people who like an item. It must return the display text as shown in the examples:

# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
from asserts.Asserts import assert_true


def likes(names):
    l = len(names)

    if not l:
        return 'no one likes this'

    if l == 1:
        return '{} likes this'.format(names[0])

    if l == 2:
        return '{} and {} like this'.format(names[0], names[1])

    if l == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])

    if l > 3:
        return '{}, {} and {} others like this'.format(names[0], names[1], l - 2)


assert_true(likes([]), 'no one likes this')
assert_true(likes(['Peter']), 'Peter likes this')
assert_true(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
assert_true(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
assert_true(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
