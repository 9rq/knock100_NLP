n = int(input())

def split_list(lst,n):
    lst_len = len(lst)
    c = lst_len // n
    size = [c for _ in range(n)]
    lst_len -= c*n
    for i in range(lst_len):
        size[i] += 1
    return size


with open('./hightemp.txt') as f:
    s = f.read()
    s = list(s.split('\n'))
    s.remove('')
    s_size = split_list(s,n)

    for i in range(n):
        ans = s[sum(s_size[:i]): sum(s_size[:i+1])]
        print(ans)
