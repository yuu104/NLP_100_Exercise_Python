from .No_30 import main_30
from typing import List

def main_32() -> List[str]:
  morphemic_sentence = main_30()

  verb_base = []
  for sentence in morphemic_sentence:
    for morpheme in sentence:
      if morpheme['pos'] == '動詞':
        verb_base.append(morpheme['base'])
  
  return verb_base

if __name__ == '__main__':
  verb_base = main_32()
  print(len(verb_base))
  print(verb_base[:30])