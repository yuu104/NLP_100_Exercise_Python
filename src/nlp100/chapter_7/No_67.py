import os
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
from pprint import pprint

def main_67():
  current_path = os.path.dirname(os.path.abspath(__file__))

  model = KeyedVectors.load_word2vec_format(f'{current_path}/../../GoogleNews/GoogleNews-vectors-negative300.bin.gz', binary=True)

  countries_vec = []
  with open(f'{current_path}/../../text/countries.txt', 'r') as f:
    for line in f:
      country_name = line.rstrip()
      country_vec = model.word_vec(country_name)
      countries_vec.append({'name': country_name, 'vec': country_vec})
  
  vec_list = [country_vec['vec'] for country_vec in countries_vec]
  kmeans = KMeans(n_clusters=5)
  kmeans.fit(vec_list)

  for index, cluster_num in enumerate(kmeans.labels_):
    print(countries_vec[index]['name'], cluster_num)

if __name__ == '__main__':
  main_67()