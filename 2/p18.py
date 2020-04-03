with open('./hightemp.txt') as f:
    lst = f.readlines()
    lst = [list(l.split('\t')) for l in lst]
    lst.sort(key= lambda x:x[2],reverse = True)
    for l in lst:
        print('\t'.join(l),end='')
