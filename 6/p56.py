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

print('recall:{}'.format(metrics.recall_score(test_y, pred_test, average=None)))
print('recall micro:{}'.format(metrics.recall_score(test_y, pred_test, average='micro')))
print('recall macro:{}'.format(metrics.recall_score(test_y, pred_test, average='macro')))
print('presicion:{}'.format(metrics.precision_score(test_y, pred_test, average=None)))
print('presicion micro:{}'.format(metrics.precision_score(test_y, pred_test, average='micro')))
print('presicion macro:{}'.format(metrics.precision_score(test_y, pred_test, average='macro')))
print('f1:{}'.format(metrics.f1_score(test_y, pred_test, average=None)))
print('f1 micro:{}'.format(metrics.f1_score(test_y, pred_test, average='micro')))
print('f1 macro:{}'.format(metrics.f1_score(test_y, pred_test, average='macro')))
