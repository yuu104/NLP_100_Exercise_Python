import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import os
import matplotlib.pyplot as plt

def main_58():
  current_path = os.path.dirname(os.path.abspath(__file__))

  results = []
  for c in np.logspace(-4, 2, 10, base=10):
    # データフレームの読み込み
    train_df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/train.feature.txt', sep='\t', index_col=0)
    valid_df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/valid.feature.txt', sep='\t', index_col=0)
    test_df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/test.feature.txt', sep='\t', index_col=0)

    # モデルの作成
    model = LogisticRegression(max_iter=1000, C=c)
    model.fit(train_df.drop('category', axis=1).values, train_df['category'].to_numpy())

    # 予測
    train_predict = model.predict(train_df.drop('category', axis=1).values)
    valid_predict = model.predict(valid_df.drop('category', axis=1).values)
    test_predict = model.predict(test_df.drop('category', axis=1).values)

    # 評価
    train_acc = accuracy_score(train_df['category'].to_numpy(), train_predict)
    valid_acc = accuracy_score(valid_df['category'].to_numpy(), valid_predict)
    test_acc = accuracy_score(test_df['category'].to_numpy(), test_predict)

    results.append([c, train_acc, valid_acc, test_acc])
  
  results = np.array(results)
  fig, ax = plt.subplots()
  ax.plot(results[:, 0], results[:, 1], label='train')
  ax.plot(results[:, 0], results[:, 2], label='valid')
  ax.plot(results[:, 0], results[:, 3], label='test')
  ax.set_xlabel('C')
  ax.set_ylabel('accuracy')
  ax.set_xscale('log')
  plt.show()

if __name__ == '__main__':
  main_58()