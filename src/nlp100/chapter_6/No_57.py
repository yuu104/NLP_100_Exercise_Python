import pandas as pd
import os
from joblib import load
import numpy as np

def main_57():
  current_path = os.path.dirname(os.path.abspath(__file__))

  model = load(f'{current_path}/../../NewsAggregatorDataset/logistic_model.joblib')

  df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/train.feature.txt', sep='\t', index_col=0)

  feature_names = df.drop('category', axis=1).columns.values

  for category, coef in zip(model.classes_, model.coef_):
    sorted_coef = np.argsort(coef)
    high_coef_index = sorted_coef[-10:][::-1]
    low_coef_index = sorted_coef[:10]
    print(f'カテゴリ: {category} ================')
    print('重みの高いトップ10')
    for i, index in enumerate(high_coef_index):
      print(f'{i + 1}\t{feature_names[index]}\t{coef[index]}')
    print('重みの低いトップ10')
    for i, index in enumerate(low_coef_index):
      print(f'{i + 1}\t{feature_names[index]}\t{coef[index]}')

if __name__ == '__main__':
  main_57()