from .No_30 import main_30
from typing import List

def main_31() -> List[str]:
  morphemic_sentence = main_30()

  verb_surface = []
  for sentence in morphemic_sentence:
    for morpheme in sentence:
      if morpheme['pos'] == '動詞':
        verb_surface.append(morpheme['surface'])
  
  return verb_surface

if __name__ == '__main__':
  verb_surface = main_31()
  print(len(verb_surface))
  print(verb_surface[:30])