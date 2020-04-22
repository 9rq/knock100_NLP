import p30
from p33 import is_noun


lst = p30.read_mecab()
ans = []

for sentence in lst:
    res = []
    for token in sentence:
        if is_noun(token):
            res.append(token['surface'])
        else:
            if len(res) > 1:
                ans.append(''.join(res))
            res = []
    else:
        if len(res) > 1:
            ans.append(''.join(res))
print(ans)
