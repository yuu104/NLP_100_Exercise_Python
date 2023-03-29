import os
from pprint import pprint
from typing import TypedDict, List

class Morpheme(TypedDict):
  surface: str
  base: str
  pos: str
  pos1: str

def main_30() -> List[List[Morpheme]]:
  path = os.path.dirname(os.path.abspath(__file__))
  with open(f'{path}/../../mecab/neko.txt.mecab', 'r') as f:
    morphemic_sentence: List[List[Morpheme]] = []
    morphemes: List[Morpheme] = []

    for line in f.readlines():
      if line == '\n':
        continue
      elif line == 'EOS\n':
        if len(morphemes) != 0:
          morphemic_sentence.append(morphemes)
        morphemes = []
        continue
      
      node = line.split('\t')
      if node[0] == '':
        continue
      feature = node[1].split(',')
      morpheme: Morpheme = {'surface': node[0], 'base': feature[6], 'pos': feature[0], 'pos1': feature[1]}
      morphemes.append(morpheme)
  
  return morphemic_sentence

if __name__ == '__main__':
  morphemic_sentence = main_30()
  
  print(len(morphemic_sentence))
  pprint(morphemic_sentence[:3])
