from collections import Counter
import p30


def get_word_frequency(lst):
    words = []
    for sentence in lst:
        for token in sentence:
            words.append(token['surface'])
    return Counter(words).most_common()

def main():
    lst = p30.read_mecab()
    ans = get_word_frequency(lst)

    print(ans)


if __name__ == '__main__':
    main()
