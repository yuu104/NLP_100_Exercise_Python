import os
from typing import List

class Morph:
  def __init__(self, line: str) -> None:
    surface, other = line.split('\t')
    others = other.split(',')
    self.surface = surface
    self.base = others[-3]
    self.pos = others[0]
    self.pos1 = others[1]

def main_40() -> List[List[Morph]]:
  current_path = os.path.dirname(os.path.abspath(__file__))

  morphs: List[Morph] = []
  sentence: List[List[Morph]] = []

  with open(f'{current_path}/../../parsed/ai.ja.txt.parsed') as f:
    for line in f:
      if line[0] == '*':
        continue
      elif line == 'EOS\n':
        if len(morphs):
          sentence.append(morphs)
          morphs = []
      else:
        morphs.append(Morph(line))
  
  return sentence

if __name__ == '__main__':
  sentence = main_40()
  for item in sentence[0]:
    print(item.__dict__)