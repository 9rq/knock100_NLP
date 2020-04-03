with open('./hightemp.txt' ) as f:
    col1  = set([])
    for line in f:
        c1,_,_,_ = line.split('\t')
        col1.add(c1)
    print(col1)
