import p30
import p35
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

show_count = 10


lst = p30.read_mecab()
lst = p35.get_word_frequency(lst)
lst = lst[:show_count]
x = range(show_count)

labels,count = zip(*lst)
print(labels, count)

fig, ax = plt.subplots()
ax.bar(x, count, tick_label = labels)
# ax.set_xticklabels(labels)
plt.show()
