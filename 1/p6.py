from p5 import *

dise = "paraparaparadise"
graph = "paragraph"

X = set(n_char_gram(dise))
Y = set(n_char_gram(graph))

union = X.union(Y)
intersection= X.intersection(Y)
diff_X = X.difference(Y)
diff_Y = Y.difference(X)

print(union)
print(intersection)
print(diff_X)
print(diff_Y)


print(tuple('se') in X)
print(tuple('se') in Y)
