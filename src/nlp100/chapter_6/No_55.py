from sklearn.metrics import confusion_matrix
# import seaborn
import pandas as pd
import os
from joblib import load

def main_55():
  current_path = os.path.dirname(os.path.abspath(__file__))

  # モデルの読み込み
  model = load(f'{current_path}/../../NewsAggregatorDataset/logistic_model.joblib')

  # データフレームの読み込み
  train_df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/train.feature.txt', sep='\t', index_col=0)
  test_df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/test.feature.txt', sep='\t', index_col=0)

  # データフレームからカテゴリのデータを取得する
  train_category = train_df['category'].to_numpy()
  test_category = test_df['category'].to_numpy()

  # 予測結果を取得
  train_predict = model.predict(train_df.drop('category', axis=1).values)
  test_predict = model.predict(test_df.drop('category', axis=1).values)
  
  # 混合行列を作成
  train_cm = confusion_matrix(train_category, train_predict)
  test_cm = confusion_matrix(test_category, test_predict)

  # 混合行列からデータフレームを作成
  train_cm_df = pd.DataFrame(train_cm, index=['b', 'e', 'm', 't'], columns=['b', 'e', 'm', 't'])
  test_cm_df = pd.DataFrame(test_cm, index=['b', 'e', 'm', 't'], columns=['b', 'e', 'm', 't'])

  print(train_cm_df)
  print(test_cm_df)

  # seaborn.heatmap(train_cm_df, vmin=0, vmax=500, annot=True, fmt='d', cmap='BuGn')
  # seaborn.heatmap(test_cm_df, vmin=0, vmax=500, annot=True, fmt='d', cmap='BuGn')

if __name__ == '__main__':
  main_55()