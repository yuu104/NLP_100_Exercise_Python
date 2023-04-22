import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main_59():
  current_path = os.path.dirname(os.path.abspath(__file__))

  train_df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/train.feature.txt', sep='\t', index_col=0)

  X_train = train_df.drop('category', axis=1).values
  y_train = train_df['category'].to_numpy()

  model = RandomForestClassifier()
  model.fit(X_train, y_train)

  test_df = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/test.feature.txt', sep='\t', index_col=0)
  
  X_test = test_df.drop('category', axis=1).values
  y_test = test_df['category'].to_numpy()

  test_predict_category = model.predict(X_test)
  
  score = accuracy_score(test_predict_category, y_test)
  print(f'正解率 : {score}')

if __name__ == '__main__':
  main_59()