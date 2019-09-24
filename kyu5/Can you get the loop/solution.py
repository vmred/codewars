# You are given a node that is the beginning of a linked list.
# This list always contains a tail and a loop.
# Your objective is to determine the length of the loop.

# For example in the following picture the tail's size is 3 and the loop size is 11.
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863


def loop_size(node):
    visited_nodes = {}
    while node not in visited_nodes:
        visited_nodes[node] = len(visited_nodes)
        node = node.next
    return len(visited_nodes) - visited_nodes[node]
