def read_mecab(file_path='../data/neko.txt.mecab'):
    res = []
    with open (file_path, 'r') as f:
        sentence = []
        for line in f:
            line = line.rstrip('\n')
            if line == 'EOS':
                break
            elif line[0] == '　':
                sentence = []
                continue
            surface, line = line.split('\t')
            line = list(line.split(','))
            d = {'surface' : surface, 'base': line[-3], 'pos' : line[0], 'pos1' : line[1]}
            sentence.append(d)
            if d['surface'] == '。':
                res.append(sentence)
                sentence = []

    return res


def main():
    res = func()
    print(res[:2])


if __name__ == '__main__':
    main()
