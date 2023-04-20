from joblib import load
import os
import pandas as pd

def main_53():
  current_path = os.path.dirname(os.path.abspath(__file__))
  
  clf = load(f'{current_path}/../../NewsAggregatorDataset/logistic_model.joblib')

  df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/valid.feature.txt', sep='\t', index_col=0)

  x = df.drop('category', axis=1).values

  print(x[0])

  probas = clf.predict_proba([x[0]])
  labels = clf.predict([x[0]])

  print(f'予測カテゴリ: {labels}')
  print(f'確率: {max(probas[0])}')

if __name__ == '__main__':
  main_53()

