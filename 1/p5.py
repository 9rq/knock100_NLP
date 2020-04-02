
def n_gram(s):
    return [tuple(s[i:i+2]) for i in range(len(s)-1)]

def n_word_gram(s):
    s = list(s.split())
    return n_gram(s)

def n_char_gram(s):
    return n_gram(s)


if __name__ == '__main__':
    s = "I am an NLPer"
    s_word = n_word_gram(s)
    s_char = n_char_gram(s)
    print(s_word)
    print(s_char)
