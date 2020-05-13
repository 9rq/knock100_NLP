import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split


#read csv
df = pd.read_csv('../data/NewsAggregatorDataset/newsCorpora.csv', header=None, sep='\t')
df.columns = ['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP']
print(df.head(2))

#extract by the PUBLISHER condition
publisher = ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']
df = df[df['PUBLISHER'].isin(publisher)]
print(df.head(2))

#sort randomly
df_s = df.sample(frac=1)
print(df_s.head(2))

#split into train,valid,test(80,10,10)
train, valid, test = np.split(df_s, [int(.8*len(df_s)), int(.9*len(df_s))])
print(len(df_s))
print(len(train))
print(len(valid))
print(len(test))


train.to_csv('../data/train.txt', sep = '\t', index = False)
valid.to_csv('../data/valid.txt', sep = '\t', index = False)
test.to_csv('../data/test.txt', sep = '\t', index = False)
