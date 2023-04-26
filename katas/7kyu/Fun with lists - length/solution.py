# Implement the method length, which accepts a linked list (head), and returns the length of the list.
# For example: Given the list: 1 -> 2 -> 3 -> 4, length should return 4.

# The linked list is defined as follows:

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# Note: the list may be null and can hold any type of value.

# Good luck!


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def length(head):
    count = 0  # Initialise count

    while head:
        count += 1
        head = head.next
    return count
