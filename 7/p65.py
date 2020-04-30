import json


def evaluate(data):
    acc = 0
    for datum in data:
        if datum['fourth'] == datum['result'][0]:
            acc += 1
    return acc/ len(data)


res = json.load(open('./p64_result.txt', 'r'))

semantic = []
syntactic = []


for key in res.keys():
    if 'gram' in key:
        syntactic += res[key]
    else:
        semantic += res[key]

print('semantic')
print(evaluate(semantic))

print('syntactic')
print(evaluate(syntactic))
