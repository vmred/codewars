# The Baum–Sweet sequence is an infinite automatic sequence of 0s and 1s defined by the rule:

# bn = 1 if the binary representation of n contains no block of consecutive 0s of odd length;
# bn = 0 otherwise;

# for n ≥ 0.

# Define a generator function baum_sweet that sequentially generates the values of this sequence.
# It will be tested for up to 1 000 000 values.
# Note that the binary representation of 0 used here is not 0 but the empty string
# ( which does not contain any blocks of consecutive 0s ).
import itertools
import re

from asserts.Asserts import assert_true


def baum_sweet():
    def odd_sequence(seq):
        if len(seq) == 0:
            return False

        for x in seq:
            if len(x) % 2:
                return True

        return False

    # for i in range(20):
    #     print('-->, bin(i): {}, regex: {}'.format(bin(i), re.findall('00*', '{0:b}'.format(i))))

    return [1 if not odd_sequence(re.findall('00*', '{0:b}'.format(i))) else 0 for i in range(20)]


assert_true(list(itertools.islice(baum_sweet(), 20)), [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1])
