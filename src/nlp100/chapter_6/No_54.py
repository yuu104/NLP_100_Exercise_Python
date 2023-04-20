from sklearn.metrics import accuracy_score
import pandas as pd
import os
from joblib import load

def main_54():
  current_path = os.path.dirname(os.path.abspath(__file__))

  df_train = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/train.feature.txt', sep='\t', index_col=0)
  df_valid = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/valid.feature.txt', sep='\t', index_col=0)
  df_test = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/test.feature.txt', sep='\t', index_col=0)

  model = load(f'{current_path}/../../NewsAggregatorDataset/logistic_model.joblib')

  predict_train = model.predict(df_train.drop('category', axis=1).values)
  predict_valid = model.predict(df_valid.drop('category', axis=1).values)
  predict_test = model.predict(df_test.drop('category', axis=1).values)

  accuracy_train = accuracy_score(df_train['category'].to_numpy(), predict_train)
  accuracy_valid = accuracy_score(df_valid['category'].to_numpy(), predict_valid)
  accuracy_test = accuracy_score(df_test['category'].to_numpy(), predict_test)

  print(f'正解率（学習データ）：{accuracy_train}')
  print(f'正解率（評価データ）：{accuracy_valid}')
  print(f'正解率（テストデータ）：{accuracy_test}')

if __name__ == '__main__':
  main_54()