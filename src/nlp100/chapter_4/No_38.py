from No_30 import main_30
import collections
from typing import List, Tuple
from matplotlib import pyplot
import japanize_matplotlib

def main_38():
  morphemic_sentences = main_30()
  
  words = []
  for sentence in morphemic_sentences:
    for morpheme in sentence:
      if morpheme['pos'] != '記号':
        words.append(morpheme['base'])

  c = collections.Counter(words)
  return list(c.values())

if __name__ == '__main__':
  commons = main_38()
  pyplot.hist(commons, range=(1, 10))
  pyplot.show()
