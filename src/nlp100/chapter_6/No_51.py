import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from pprint import pprint

def clean_text(text: str):
  text = re.sub(r'\d+', '', text)  # 数字
  text = re.sub(r'[!-/:-@[-`{-~]', '', text)  # 記号
  text = re.sub(r'[︰-＠]', '', text)  # 全角記号
  text = re.sub(r'[「」【】『』“”‘’()（）\[\]【】<>＜＞〈〉〔〕〘〙〚〛]', '', text)  # 括弧
  text = text.lower()
  return text

def main_51():
  current_path = os.path.dirname(os.path.abspath(__file__))

  data_list = []
  category_list = []
  len_train = 0
  len_valid = 0
  len_test = 0

  with open(f'{current_path}/../../NewsAggregatorDataset/train.txt', 'r') as f:
    for line in f:
      sentence = line.split('\t')[1].rstrip('\n')
      sentence = clean_text(sentence)
      data_list.append(sentence)
      category_list.append(line.split('\t')[0])
      len_train += 1

  with open(f'{current_path}/../../NewsAggregatorDataset/valid.txt', 'r') as f:
    for line in f:
      sentence = line.split('\t')[1].rstrip('\n')
      sentence = clean_text(sentence)
      data_list.append(sentence)
      category_list.append(line.split('\t')[0])
      len_valid += 1
  
  with open(f'{current_path}/../../NewsAggregatorDataset/valid.txt', 'r') as f:
    for line in f:
      sentence = line.split('\t')[1].rstrip('\n')
      sentence = clean_text(sentence)
      data_list.append(sentence)
      category_list.append(line.split('\t')[0])
      len_test += 1
  
  vec_tfidf = TfidfVectorizer()

  # ベクトル化
  vec = vec_tfidf.fit_transform(data_list)

  # pandasでデータフレームを作成
  df = pd.DataFrame(vec.toarray(), columns=vec_tfidf.get_feature_names_out())
    
  # 先頭にcategoryカラムを追加
  df.insert(0, 'category', category_list)

  train_df = df.iloc[:len_train, :]
  valid_df = df.iloc[len_train:len_train + len_valid, :]
  test_df = df.iloc[len_train + len_valid:, :]
  pprint(train_df)
  pprint(valid_df)
  pprint(test_df)

  train_df.to_csv(f'{current_path}/../../NewsAggregatorDataset/train.feature.txt', sep='\t')
  valid_df.to_csv(f'{current_path}/../../NewsAggregatorDataset/valid.feature.txt', sep='\t')
  test_df.to_csv(f'{current_path}/../../NewsAggregatorDataset/test.feature.txt', sep='\t')

if __name__ == '__main__':
  main_51()
  print("終了")