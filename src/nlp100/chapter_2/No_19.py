from typing import List
import os
import collections

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))

  data: List[str] = []
  with open(f'{path}/../../text/popular-names.txt') as f:
    for line in f:
      data.append(line.split('\t')[0])
  
  c = collections.Counter(data)
  print(c.most_common())

