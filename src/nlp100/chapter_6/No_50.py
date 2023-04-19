import os
from pprint import pprint
import random
import numpy as np

def main_50():
  current_path = os.path.dirname(os.path.abspath(__file__))

  publishers = [
    'Reuters',
    'Huffington Post',
    'Businessweek',
    'Contactmusic.com',
    'Daily Mail',
  ]

  data = []

  with open(f'{current_path}/../../NewsAggregatorDataset/newsCorpora.csv', 'r') as f:
    for line in f:
      elements = line.split('\t')
      if elements[3] in publishers:
        data.append(elements)
  
  random.shuffle(data)
  
  np_array_data = np.array(data)
  train_data, valid_data, test_data = np.split(np_array_data, [int(len(np_array_data) * 0.8), int(len(np_array_data) * 0.9)])

  with open(f'{current_path}/../../NewsAggregatorDataset/train.txt', 'w') as f:
    for line in train_data:
      f.write(f'{line[4]}\t{line[1]}\n')
  
  with open(f'{current_path}/../../NewsAggregatorDataset/valid.txt', 'w') as f:
    for line in valid_data:
      f.write(f'{line[4]}\t{line[1]}\n')

  with open(f'{current_path}/../../NewsAggregatorDataset/test.txt', 'w') as f:
    for line in test_data:
      f.write(f'{line[4]}\t{line[1]}\n')

if __name__ == '__main__':
  main_50()