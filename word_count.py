import urllib.request as urlreq
import conf
import keyword
from matplotlib import pyplot as plt
import operator

def print_frequency(word_frequency):
    for words in sorted(word_frequency):
        count = word_frequency[words]
        print(words, " : ",  count)

def plot_frequency(word_frequency):
   # lists = sorted(word_frequency.items(), key=operator.itemgetter(0))
    lists = sorted(word_frequency.items())
    x, y = zip(*lists) 
    plt.plot(x, y)
    plt.show()

word_frequency = {}

with urlreq.urlopen(conf.URL) as page:
    for line in page:
        line = line.strip().decode("utf-8")
        if len(line) > 0:
            line_words = line.split(" ")

        for word in line_words: 
            if (word in word_frequency) and (word in conf.python_keywords): 
                word_frequency[word] = word_frequency[word] + 1
            elif word in conf.python_keywords:
                word_frequency[word] = 1

print_frequency(word_frequency)

plot_frequency(word_frequency)

