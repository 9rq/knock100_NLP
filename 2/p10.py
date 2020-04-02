count = 0
with open('./hightemp.txt') as f:
    for _ in f:
        count += 1
print(count)
