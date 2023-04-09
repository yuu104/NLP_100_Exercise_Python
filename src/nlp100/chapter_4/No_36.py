from matplotlib import pyplot
import japanize_matplotlib
from .No_35 import main_35

def main_36():
  freq_words = main_35()
  x = []
  y = []
  for word in freq_words:
    x.append(word[0])
    y.append(word[1])
  
  pyplot.bar(x, y)
  pyplot.show()

if __name__ == '__main__':
  main_36()