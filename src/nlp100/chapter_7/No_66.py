import os
from gensim.models import KeyedVectors
from scipy.stats import spearmanr

def main_66():
  current_path = os.path.dirname(os.path.abspath(__file__))

  model = KeyedVectors.load_word2vec_format(f'{current_path}/../../GoogleNews/GoogleNews-vectors-negative300.bin.gz', binary=True)

  human = []
  w2v = []

  with open(f'{current_path}/../../text/combined.csv') as f:
    next(f)
    for line in f:
      data = line.rstrip().split(',')
      human.append(float(data[-1]))
      w2v.append(model.similarity(data[0], data[1]))

  correlation, pvalue = spearmanr(human, w2v)
  print('スピアマン相関係数: {}'.format(correlation))

if __name__ == '__main__':
  main_66()