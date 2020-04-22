import p30


lst = p30.read_mecab()
ans = []

def search(lst,key1,key2,key3):
    res = []
    for sentence in lst:
        for token in sentence:
            if token[key1] == key2:
                res.append(token[key3])
    return res

res = search(lst,'pos','動詞', 'surface')
print(res)
