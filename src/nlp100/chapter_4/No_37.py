from .No_30 import main_30
import collections
from pprint import pprint
from matplotlib import pyplot
import japanize_matplotlib

def main_37():
  morphemic_sentences = main_30()
  
  cooccurrence_list = []
  for sentence in morphemic_sentences:
    if [item for item in sentence if item['base'] == '猫']:
      cooccurrence_list.extend([word['surface'] for word in sentence])
  
  c = collections.Counter(cooccurrence_list)
  return c.most_common(10)

if __name__ == '__main__':
  cooccurrence_list = main_37()
  x = []
  y = []
  for word in cooccurrence_list:
    x.append(word[0])
    y.append(word[1])
  
  pyplot.bar(x, y)
  pyplot.show()

