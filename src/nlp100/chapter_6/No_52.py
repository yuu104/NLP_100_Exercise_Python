from sklearn.linear_model import LogisticRegression
import os
import pandas as pd
from joblib import dump

def main_52():
  current_path = os.path.dirname(os.path.abspath(__file__))

  df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/train.feature.txt', sep='\t', index_col=0)

  x = df.drop('category', axis=1).values
  y = df['category'].to_numpy()

  clf = LogisticRegression()
  clf.fit(x, y)

  dump(clf, f'{current_path}/../../NewsAggregatorDataset/logistic_model.joblib')

if __name__ == '__main__':
  main_52()