from typing import List
import os

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))
  f = open(f'{path}/../../text/popular-names.txt')
  data = f.read().splitlines()
  data_lists: List[List[str]] = []
  for line in data:
    data_lists.append(line.split('\t'))

  data_lists = sorted(data_lists, key=lambda x: int(x[2]), reverse=True)
  print(data_lists[:5])

  f.close()