import pandas as pd
from sklearn import metrics
import p53
import joblib

vocab = joblib.load('./model/vocabulary.joblib')
vocab = list(vocab.items())
vocab.sort(key = lambda x:x[1])
vocab = [[-1,-1]] + vocab

clf = p53.load_model()

print(len(clf.coef_))
for cls in clf.coef_:
    cls = [(cls[i], vocab[i]) for i in range(len(cls))]
    cls.sort()
    print(cls[-10:])
    print(cls[:10])
