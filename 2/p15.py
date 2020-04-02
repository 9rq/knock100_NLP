n = int(input())

with open('./hightemp.txt') as f:
    s = f.read()
    s = s.split('\n')
    print('\n'.join(s[-n-1:]),end= '')
