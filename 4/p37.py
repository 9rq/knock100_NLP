import p30
import p36
from collections import Counter


lst = p30.read_mecab()

words = []

for sentence in lst:
    flag = 0
    res = []
    for token in sentence:
        if not flag and token['base'] == '猫':
            flag = 1
        if token['pos'] == '名詞':
            res.append(token['base'])
    if flag:
        res.remove('猫')
        words.extend(res)

words = Counter(words).most_common()
words = words[:10]
label, count = zip(*words)
p36.plot(count, label, 10)
