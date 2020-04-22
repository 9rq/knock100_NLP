import p30
import p35
import matplotlib.pyplot as plt


def plot_hist(count):
    fig, ax = plt.subplots()
    ax.hist(count, bins = 100)
    plt.show()


lst = p30.read_mecab()
lst = p35.get_word_frequency(lst)
lst = [x[1] for x in lst]
plot_hist(lst)
