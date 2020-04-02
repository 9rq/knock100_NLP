def output_col(path,col):
    with open(path,'w') as f:
        f.write('\n'.join(col))
    return

with open('./hightemp.txt') as f:
    col1 = []
    col2 = []
    for line in f:
        c1,c2,_,_ = line.split('\t')
        col1.append(c1)
        col2.append(c2)
    output_col('col1.txt',col1)
    output_col('col2.txt',col2)

