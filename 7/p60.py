import gensim


def read_vectors(file_path='./GoogleNews-vectors-negative300.bin'):
    model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)
    return model


def main():
    res = read_vectors()
    print('United_States')
    print(res['United_States'])


if __name__ == '__main__':
    main()
