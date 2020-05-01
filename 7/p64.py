import p60
import json


output_path = './p64_result.txt'
model = p60.read_vectors()
ans = {}


with open('../data/questions-words.txt', 'r') as f:

    res = []
    for line in f:
        if line[0] == ':':
            if res:
                ans[key] = res
                res = []
            key = line
            continue
        line = line.rstrip('\n')
        first, second, third, fourth = line.split()
        d = {'first':first, 'second':second, 'third':third, 'fourth':fourth}
        d['result'] = model.most_similar(positive=[second, third], negative = [first], topn=1)[0]
        print(d)
        res.append(d)

json.dump(ans, open(output_path, 'w'))
