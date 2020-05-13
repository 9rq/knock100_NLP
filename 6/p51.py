import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


publisher = ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']
category = ['b', 'e', 't', 'm']


def list_to_dict(lst):
    return dict([[lst[i], i] for i in range(len(lst))])


def read_data(file_path):
    dataset = pd.read_csv(file_path, sep = '\t')
    dataset = dataset[['TITLE','PUBLISHER','CATEGORY']]

    publisher_d = list_to_dict(publisher)
    category_d = list_to_dict(category)

    dataset['PUBLISHER'] = dataset['PUBLISHER'].map(publisher_d)
    dataset['CATEGORY'] = dataset['CATEGORY'].map(category_d)

    return dataset


def func(train, test, valid):
    train['TMP'] = 'train'
    test['TMP'] = 'test'
    valid['TMP'] = 'valid'
    dataset = pd.concat([train,test,valid]).reset_index(drop=True)

    vectorizer = CountVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
    bag = vectorizer.fit_transform(dataset['TITLE'])
    dataset = pd.concat([dataset, pd.DataFrame(bag.toarray())], axis = 1)
    train = dataset[dataset['TMP'] == 'train'].drop(['TMP'], axis = 1)
    test = dataset[dataset['TMP'] == 'test'].drop(['TMP'], axis = 1)
    valid = dataset[dataset['TMP'] == 'valid'].drop(['TMP'], axis = 1)
    train.to_csv('../data/train.feature.txt', index = False)
    valid.to_csv('../data/valid.feature.txt', index = False)
    test.to_csv('../data/test.feature.txt', index = False)

def main():
    train = read_data('../data/train.txt')
    valid = read_data('../data/valid.txt')
    test = read_data('../data/test.txt')
    func(train, test, valid)


if __name__ == '__main__':
    main()
