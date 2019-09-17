# Given an input n, write a function always that returns a function which returns n.
# Ruby should return a lambda or a proc.


def always(n=0):
    def r():
        return n

    return r
