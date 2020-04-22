import p30
import p35
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

show_count = 10


def plot(count,labels,show_count):
    fig, ax = plt.subplots()
    ax.bar(range(show_count), count, tick_label = labels)
    plt.show()

lst = p30.read_mecab()
lst = p35.get_word_frequency(lst)
lst = lst[:show_count]

labels,count = zip(*lst)

plot(count,labels,10)
