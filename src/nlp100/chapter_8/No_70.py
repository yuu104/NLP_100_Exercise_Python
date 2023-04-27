import os
import pandas as pd
from sklearn.model_selection import train_test_split
import re
import numpy as np
from gensim.models import KeyedVectors
import torch
from pprint import pprint

# テキストの前処理
def preprocessing(text):
  text_clean = re.sub(r'[\"\'.,:;\(\)#\|\*\+\!\?#$%&/\]\[\{\}]', '', text)
  text_clean = re.sub('[0-9]+', '0', text_clean)
  return text_clean

def main_70():
  current_path = os.path.dirname(os.path.abspath(__file__))

  data = pd.read_csv(f'{current_path}/../../NewsAggregatorDataset/newsCorpora.csv', header=None, sep='\t', names=['ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'])

  # 特定の情報源（publisher）のみ抽出
  publishers = ['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']
  data = data.loc[data['PUBLISHER'].isin(publishers), ['TITLE', 'CATEGORY']].reset_index(drop=True)
  
  # 学習用、検証用、評価用に分割する
  train, valid_test = train_test_split(data, test_size=0.2, shuffle=True, random_state=64, stratify=data['CATEGORY'])
  valid, test = train_test_split(valid_test, test_size=0.5, shuffle=True, random_state=64, stratify=valid_test['CATEGORY'])

  train = train.reset_index(drop=True)
  valid = valid.reset_index(drop=True)
  test = test.reset_index(drop=True)

  # データの結合
  df = pd.concat([train, valid, test], axis=0).reset_index(drop=True) 

  # 記事タイトルの前処理
  df['TITLE'] = df['TITLE'].apply(preprocessing)

  model = KeyedVectors.load_word2vec_format(f'{current_path}/../../GoogleNews/GoogleNews-vectors-negative300.bin.gz', binary=True)

  # 平均単語ベクトルの取得
  def w2v(text):
    words = text.rstrip().split()
    vec = [model[word] for word in words if word in model]
    return np.array(sum(vec) / len(vec))

  vecs = np.array([])
  for text in df['TITLE']:
    if len(vecs) == 0:
        vecs = w2v(text)
    else:
        vecs = np.vstack([vecs, w2v(text)])
  
  # データのテンソル化
  X_train = torch.tensor(vecs[:len(train), :])
  X_valid = torch.tensor(vecs[len(train):len(train) + len(valid), :])
  X_test = torch.tensor(vecs[len(train) + len(valid): , :])

  # ターゲットのテンソル化
  category_dict = {'b': 0, 't': 1, 'e':2, 'm':3}
  Y_train = torch.from_numpy(train['CATEGORY'].map(category_dict).values)
  Y_valid = torch.from_numpy(valid['CATEGORY'].map(category_dict).values)
  Y_test = torch.from_numpy(test['CATEGORY'].map(category_dict).values)

  torch.save(X_train, f'{current_path}/../../NewsAggregatorDataset/chapter_8/X_train.pt')
  torch.save(X_valid, f'{current_path}/../../NewsAggregatorDataset/chapter_8/X_valid.pt')
  torch.save(X_test, f'{current_path}/../../NewsAggregatorDataset/chapter_8/X_test.pt')
  torch.save(Y_train, f'{current_path}/../../NewsAggregatorDataset/chapter_8/y_train.pt')
  torch.save(Y_valid, f'{current_path}/../../NewsAggregatorDataset/chapter_8/y_valid.pt')
  torch.save(Y_test, f'{current_path}/../../NewsAggregatorDataset/chapter_8/y_test.pt')

if __name__ == '__main__':
  main_70()