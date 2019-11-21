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
