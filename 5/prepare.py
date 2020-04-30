import CaboCha


file_path = 'neko.txt'
output_path = file_path + '.cabocha'
cabocha = CaboCha.Parser()


def func(file_path, output_path):
    with open(file_path, 'r') as input_file, open(output_path, 'w') as output_file:
        output_file.write(cabocha.parse(input_file.read()).toString(CaboCha.FORMAT_LATTICE))


def main():
    func(file_path, output_path)


if __name__ == '__main__':
    main()
