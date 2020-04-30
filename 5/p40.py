from util import Morph


def read_cabocha_morph(file_path = './neko.txt.cabocha'):
    sentences = []

    with open(file_path, 'r') as f:
        sent  = []
        for line in f:
            if line[0] =='*' or line == 'EOS\n':
                continue
            surface, line = line.split('\t')
            line = list(line.split(','))
            base = line[-3]
            pos = line[0]
            pos1 = line[1]

            morph = Morph(surface, base, pos, pos1)

            sent.append(morph)
            if surface == '。':
                sentences.append(sent)
                sent = []

    return sentences



def main():
    res = read_cabocha_morph()
    print(res[:3])


if __name__ == '__main__':
    main()
