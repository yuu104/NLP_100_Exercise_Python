import os
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text: str):
  text = re.sub(r'\d+', '', text)  # 数字
  text = re.sub(r'[!-/:-@[-`{-~]', '', text)  # 記号
  text = re.sub(r'[︰-＠]', '', text)  # 全角記号
  text = re.sub(r'[「」【】『』“”‘’()（）\[\]【】<>＜＞〈〉〔〕〘〙〚〛]', '', text)  # 括弧
  text = text.lower()
  return text

def main_51():
  current_path = os.path.dirname(os.path.abspath(__file__))

  with open(f'{current_path}/../../NewsAggregatorDataset/train.txt', 'r') as f:
    train_list = []
    category_list = []

    for line in f:
      sentence = line.split('\t')[1].rstrip('\n')
      sentence = clean_text(sentence)
      train_list.append(sentence)
      category_list.append(line.split('\t')[0])

    vec_tfidf = TfidfVectorizer()

    # ベクトル化
    vec = vec_tfidf.fit_transform(train_list)

    # pandasでデータフレームを作成
    df = pd.DataFrame(vec.toarray(), columns=vec_tfidf.get_feature_names_out())
    
    # 先頭にcategoryカラムを追加
    df.insert(0, 'category', category_list)

    df.to_csv(f'{current_path}/../../NewsAggregatorDataset/train.feature.txt', sep='\t')

  with open(f'{current_path}/../../NewsAggregatorDataset/valid.txt', 'r') as f:
    valid_list = []
    category_list = []

    for line in f:
      sentence = line.split('\t')[1].rstrip('\n')
      sentence = clean_text(sentence)
      valid_list.append(sentence)
      category_list.append(line.split('\t')[0])

    vec_tfidf = TfidfVectorizer()

    # ベクトル化
    vec = vec_tfidf.fit_transform(valid_list)

    # pandasでデータフレームを作成
    df = pd.DataFrame(vec.toarray(), columns=vec_tfidf.get_feature_names_out())
    
    # 先頭にcategoryカラムを追加
    df.insert(0, 'category', category_list)

    df.to_csv(f'{current_path}/../../NewsAggregatorDataset/valid.feature.txt', sep='\t')
  
  with open(f'{current_path}/../../NewsAggregatorDataset/valid.txt', 'r') as f:
    test_list = []
    category_list = []

    for line in f:
      sentence = line.split('\t')[1].rstrip('\n')
      sentence = clean_text(sentence)
      test_list.append(sentence)
      category_list.append(line.split('\t')[0])

    vec_tfidf = TfidfVectorizer()

    # ベクトル化
    vec = vec_tfidf.fit_transform(test_list)

    # pandasでデータフレームを作成
    df = pd.DataFrame(vec.toarray(), columns=vec_tfidf.get_feature_names_out())
    
    # 先頭にcategoryカラムを追加
    df.insert(0, 'category', category_list)

    df.to_csv(f'{current_path}/../../NewsAggregatorDataset/test.feature.txt', sep='\t')

if __name__ == '__main__':
  main_51()
  print("終了")