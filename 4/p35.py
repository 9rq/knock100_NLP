from collections import Counter
import p30


lst = p30.read_mecab()

words = []
for sentence in lst:
    for token in sentence:
        words.append(token['surface'])
ans = Counter(words).most_common()
print(ans)

