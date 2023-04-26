import os
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

def main_68():
  current_path = os.path.dirname(os.path.abspath(__file__))

  model = KeyedVectors.load_word2vec_format(f'{current_path}/../../GoogleNews/GoogleNews-vectors-negative300.bin.gz', binary=True)

  countries_vec = []
  with open(f'{current_path}/../../text/countries.txt', 'r') as f:
    for line in f:
      country_name = line.rstrip()
      country_vec = model.word_vec(country_name)
      countries_vec.append({'name': country_name, 'vec': country_vec})
  
  vec_list = [country_vec['vec'] for country_vec in countries_vec]
  country_name_list = [country_vec['name'] for country_vec in countries_vec]
  
  linkage_result = linkage(vec_list, method='ward')

  plt.figure(figsize=(16, 9))
  dendrogram(linkage_result, labels=country_name_list)
  plt.savefig('fig68.png')
  plt.show()

if __name__ == '__main__':
  main_68()