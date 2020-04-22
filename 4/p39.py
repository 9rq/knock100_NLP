import p30
import p35
import matplotlib.pyplot as plt


def plot(lst):
    fig, ax = plt.subplots()
    ax.scatter(range(1,len(lst)+1), lst)
    ax.set_xscale('log')
    ax.set_yscale('log')

    plt.show()

lst = p30.read_mecab()
lst = p35.get_word_frequency(lst)
lst = [x[1] for x in lst]

plot(lst)
