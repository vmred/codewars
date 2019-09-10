# Greed is good
# Greed is a dice game played with five six-sided dice.
# Your mission, should you choose to accept it, is to score a throw according to these rules.
# You will always be given an array with five six-sided dice values.

# Three 1's => 1000 points
# Three 6's =>  600 points
# Three 5's =>  500 points
# Three 4's =>  400 points
# Three 3's =>  300 points
# Three 2's =>  200 points
# One   1   =>  100 points
# One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a "5" can only count as part of a triplet
# (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

# Example scoring

# Throw       Score
# ---------   ------------------
# 5 1 3 4 1   50 + 2 * 100 = 250
# 1 1 1 3 1   1000 + 100 = 1100
# 2 4 4 5 4   400 + 50 = 450


def score(dice):
    # dice = str(dice)
    dice = ''.join(list(map(str, dice)))
    print('--> dice:', dice)
    rules = {
        '1': 100,
        '5': 50,
        '1, 1, 1': 1000,
        '6, 6, 6': 600,
        '5, 5, 5': 500,
        '4, 4, 4': 400,
        '3, 3, 3': 200,
        '2, 2, 2': 200
    }
    #
    # result = 0
    # for k, v in rules.items():
    #     # if k == '4, 4, 4':
    #     #     print('---> 4, 4, 4 in dice:', k in dice)
    #     if k in dice:
    #         # print('--> k in dice, k: {}'.format(k))
    #         result += v
    #         dice.replace(k, '')
    #         # print('--> dice after replacing:', dice)

    result = 0

    while dice != '':
        if '1' in dice:
            count = dice.count('1')
            print('--> count:', count)

            if count == 1:
                result += 50
                dice.replace('1', '')

            if count == 3:
                result += 1000
                dice.replace('111', '')

            print('---> dice after replacing:', dice)

    return result
