import p30


def is_noun(token):
    return token['pos'] == '名詞'

lst = p30.read_mecab()

ans = []
for sentence in lst:
    for i in range(len(sentence)-2):
        if is_noun(sentence[i]) and sentence[i+1]['surface']=='の' and is_noun(sentence[i+2]):
            ans.append(sentence[i]['surface'] + 'の' + sentence[i+2]['surface'])
print(ans)
