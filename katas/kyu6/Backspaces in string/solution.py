def clean_string(s):
    s = list(s)

    while '#' in s:
        pos = s.index('#')

        if pos == 0:
            s.pop(pos)

        else:
            s.pop(pos - 1)
            s.pop(pos - 1)

    return ''.join(s)
