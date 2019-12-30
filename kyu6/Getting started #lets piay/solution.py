# Well, for my first kata, I did a mess. Would you help me, please, to make my code work ?

# I'm sure I didn't mix the numbers, but all the rest...


from math import pi


def whatpimeans(alpha='abcdefghijklmnopqrstuvwxyz'):
    dico = {k: v for k, v in
            zip([85, 24, 32, 64, 11, 52, 91, 79, 78, 99, 62, 27, 74, 35, 14,
                 16, 66, 81, 19, 39, 13, 33, 45, 49, 95, 10], alpha.upper())}

    crypt = str(pi).replace('.', '')[::-1]
    code = [int(crypt[i:i + 2]) for i in range(0, len(crypt), 2)]
    return ''.join([dico[x] for x in code])
