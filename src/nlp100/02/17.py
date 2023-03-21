import os
from typing import List

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))

  f = open(f'{path}/../../text/popular-names.txt')
  data = f.readlines()

  names: List[str] = []
  for line in data:
    names.append(line.split('\t')[0])

  print(len(list(dict.fromkeys(names))))
  
  f.close()
