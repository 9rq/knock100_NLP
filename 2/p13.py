with open('./col1.txt')as f1:
    with open('./col2.txt') as f2:
        with open('ans13.txt' ,'w') as f3:
            for c1,c2 in zip(f1,f2):
                f3.write('\t'.join((c1[:-1],c2)))
