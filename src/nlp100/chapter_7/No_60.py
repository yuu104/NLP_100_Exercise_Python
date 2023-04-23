import os
from gensim.models import KeyedVectors

def main_60():
  current_path = os.path.dirname(os.path.abspath(__file__))
  
  model = KeyedVectors.load_word2vec_format(f'{current_path}/../../GoogleNews/GoogleNews-vectors-negative300.bin.gz', binary=True)

  print(model['United_States'])

if __name__ == '__main__':
  main_60()