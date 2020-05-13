import pandas as pd
from sklearn import metrics
import p53



train = pd.read_csv('../data/train.feature.txt')
train_y = train['CATEGORY']
train_x = train.drop(['TITLE', 'CATEGORY'], axis = 1)

test = pd.read_csv('../data/test.feature.txt')
test_y = test['CATEGORY']
test_x = test.drop(['TITLE', 'CATEGORY'], axis = 1)

clf = p53.load_model()
pred_train = clf.predict(train_x)
pred_test = clf.predict(test_x)

result_train = metrics.confusion_matrix(train_y, pred_train)
print(result_train)

result_test = metrics.confusion_matrix(test_y, pred_test)
print(result_test)
