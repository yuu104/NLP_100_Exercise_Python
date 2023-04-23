import os
from gensim.models import KeyedVectors
from pprint import pprint

def main_63():
  current_path = os.path.dirname(os.path.abspath(__file__))
  
  model = KeyedVectors.load_word2vec_format(f'{current_path}/../../GoogleNews/GoogleNews-vectors-negative300.bin.gz', binary=True)

  similar_words = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
  pprint(similar_words)

if __name__ == '__main__':
  main_63()