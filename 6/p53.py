import pandas as pd
import joblib

def load_model(file_path = './model/model.joblib'):
    return joblib.load(file_path)


def main():
    clf = joblib.load('./model/model.joblib')

    train = pd.read_csv('../data/train.feature.txt')
    train_y = train['CATEGORY']
    train_x = train.drop(['TITLE', 'CATEGORY'], axis = 1)

    pred = clf.predict(train_x)
    print(pred)

if __name__ == '__main__':
    main()
