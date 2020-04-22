import p30
import p31


lst = p30.read_mecab()
ans = []

res = p31.search(lst,'pos','動詞', 'base')
print(res)
