import re
with open('./hightemp.txt') as f:
    s = f.read()
    s = re.sub('\t', ' ',s)
    print(s)
