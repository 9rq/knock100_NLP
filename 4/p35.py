from collections import Counter
import p30


lst = p30.read_mecab()

words = []
for sentence in lst:
    for token in sentence:
        words.append(token['surface'])
ans = list(Counter(words).items())
ans.sort(key = lambda x:x[1], reverse = 1)
print(ans)

