# Bob is preparing to pass IQ test.
# The most frequent task in this test is to find out which one of the given numbers differs from the others.
# Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers
# finds one that is different in evenness, and return a position of this number.

# Keep in mind that your task is to help Bob solve a real IQ test,
# which means indexes of the elements start from 1 (not 0)


def iq_test(numbers):
    e = [int(i) % 2 for i in numbers.split()]
    return e.index(1) + 1 if e.count(1) == 1 else e.index(0) + 1


print(iq_test("2 4 7 8 10"))
