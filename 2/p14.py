n = int(input())

with open ('./hightemp.txt') as f:
    for i in range(n):
        print(f.readline(),end = '')
