import os
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from typing import List
import numpy as np

def main_69():
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
    
    pca = PCA(n_components=10)
    vec_pca = pca.fit_transform(np.array(vec_list))

    tsne = TSNE(n_components=2, perplexity=30.0, early_exaggeration=12.0)
    vec_tsne = tsne.fit_transform(vec_pca)

    plt.figure(figsize=(12, 8))
    plt.scatter(vec_tsne[:, 0], vec_tsne[:, 1], c='b', alpha=0.5)

    for i, txt in enumerate(country_name_list):
      plt.annotate(txt, (vec_tsne[i, 0], vec_tsne[i, 1]))

    plt.show()

if __name__ == '__main__':
  main_69()