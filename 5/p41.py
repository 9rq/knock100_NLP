from util import Morph
from util import Chunk


def read_cabocha(file_path = './neko.txt.cabocha'):
    with open(file_path, 'r') as f:
        sent = []
        chunk = None
        for line in f:
            if line[0] == '*':
                if chunk is not None:
                    sent.append(chunk)
                chunk = Chunk()
                continue
            elif line == 'EOS\n':
                continue

            surface, line = line.split('\t')
            line = list(line.split(','))
            base = line[-3]
            pos = line[0]
            pos1 = line[1]
            morph = Morph(surface, base, pos, pos1)
            chunk.morphs.append(morph)

        pass


def main():
    res = read_cabocha()
    print(res[8])


if __name__ == '__main__':
    main()
