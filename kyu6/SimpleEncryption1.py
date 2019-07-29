def encrypt(text, n):
    if not text:
        return text

    for _ in range(n):
        text = text[1::2] + text[::2]
    return text


def decrypt(encrypted_text, n):
    if not encrypted_text:
        return encrypted_text

    o, l = len(encrypted_text) // 2, list(encrypted_text)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)


# print(encrypt('This is a test!', 1))
# print(decrypt('hsi  etTi sats!', 1))

a = encrypt('This is a test!', 1)
e = 'hsi  etTi sats!'
assert (a == e), '--> actual: %s, expected %s' % (a, e)

a = decrypt('hsi  etTi sats!', 1)
e = 'This is a test!'
assert (a == e), '--> actual: %s, expected %s' % (a, e)

a = encrypt('This is a test!', 3)
e = ' Tah itse sits!'
assert (a == e), '--> actual: %s, expected %s' % (a, e)
