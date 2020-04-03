from collections import Counter
with open('./hightemp.txt') as f:
    col1 = []
    for line in f:
        c1,_,_,_ = line.split('\t')
        col1.append(c1)
    count = Counter(col1)
    ans = sorted(count.items(),key = lambda x : x[1])
    for a in ans:
        print(*a)
