def is_alphabet(c):
    return 'a'<= c <= 'z'

def cigher(s):
    res = ''
    for c in s:
        if is_alphabet(c):
            res += chr(219-ord(c))
        else:
            res += c
    return res

s = 'abcABC123+-*/'
print(s)
s = cigher(s)
print(s)
s = cigher(s)
print(s)
