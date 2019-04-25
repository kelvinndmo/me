def inv(c):
    if 'a' <= c <= 'z':
        print(chr(122 - ord(c) + 97))
    if 'A' <= c <= 'Z':
        print(chr(90 - ord(c) + 65))
    return c


''.join(inv(c) for c in 'az')
