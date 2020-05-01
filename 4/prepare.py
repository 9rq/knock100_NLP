import MeCab


file_path = '../data/neko.txt'
output_path = file_path + '.mecab'

mecab = MeCab.Tagger()


def func(file_path, output_path):
    with open(file_path,'r') as input_file, open(output_path,'w') as output_file:
        output_file.write(mecab.parse(input_file.read()))


def main():
    func(file_path, output_path)

if __name__ == '__main__':
    main()
