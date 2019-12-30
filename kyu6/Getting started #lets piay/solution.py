# Well, for my first kata, I did a mess. Would you help me, please, to make my code work ?

# I'm sure I didn't mix the numbers, but all the rest...


from math import pi


def whatpimeans(alpha='abcdefghijklmnopqrstuvwxyz'):
    # create a dictionnary linking alphabet to 'secret encryption'
    # dico = {85:'a', 24:'b',32:'c', [...],10:'z'}
    dico = {k: v for k, v in
            zip([85, 24, 32, 64, 11, 52, 91, 79, 78, 99, 62, 27, 74, 35, 14,
                 16, 66, 81, 19, 39, 13, 33, 45, 49, 95, 10], alpha.upper())}

    # take the number PI as string and prepare it for decoding
    crypt = str(pi).replace('.', '')[::-1]
    # reverse the string and group 2 by 2 to form a list
    code = [int(crypt[i:i+2]) for i in range(0, len(crypt), 2)]

    # take the modified string and try to decode

    decrypt = ''.join([dico[x] for x in code])
    # stuck somewhere ? try to print() some of the steps
    return decrypt
