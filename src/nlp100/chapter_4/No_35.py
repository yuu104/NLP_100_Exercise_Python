from .No_30 import main_30
import collections
from typing import List, Tuple

def main_35() -> List[Tuple[str, int]]:
  morphemic_sentences = main_30()
  
  words = []
  for sentence in morphemic_sentences:
    for morpheme in sentence:
      if morpheme['pos'] != '記号':
        words.append(morpheme['base'])

  c = collections.Counter(words)
  return c.most_common(10)

if __name__ == '__main__':
  print(main_35())