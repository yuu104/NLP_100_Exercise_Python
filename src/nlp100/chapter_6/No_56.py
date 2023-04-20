from sklearn.metrics import classification_report
import pandas as pd
import os
from joblib import load

def main_56():
  current_path = os.path.dirname(os.path.abspath(__file__))

  # モデルの読み込み
  model = load(f'{current_path}/../../NewsAggregatorDataset/logistic_model.joblib')

  # データフレームの読み込み
  test_df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/test.feature.txt', sep='\t', index_col=0)

  # データフレームからカテゴリのデータを取得する
  test_category = test_df['category'].to_numpy()

  # 予測結果を取得
  test_predict = model.predict(test_df.drop('category', axis=1).values)

  print(classification_report(test_category, test_predict, labels=['b', 'e', 'm', 't']))

if __name__ == '__main__':
  main_56()