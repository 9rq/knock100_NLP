import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
import joblib


train = pd.read_csv('../data/train.feature.txt')
train_y = train['CATEGORY']
train_x = train.drop(['TITLE', 'CATEGORY'], axis = 1)
print(train_x.head(3))
print(train_y.head(3))

clf = LogisticRegression(penalty='l2', solver = 'sag', random_state = 0)
clf.fit(train_x, train_y)
joblib.dump(clf, './model/model.joblib')
