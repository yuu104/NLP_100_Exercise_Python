import os
from typing import List
from No_41 import main_41

def main_45():
  current_path = os.path.dirname(os.path.abspath(__file__))
  sentences = main_41()
  
  with open(f'{current_path}/../../text/result_45.txt', 'w') as f:
    for sentence in sentences:
      for chunk in sentence:
        verb_morphs = [morph for morph in chunk.morphs if morph.pos == '動詞']
        if len(verb_morphs) == 0 or len(chunk.srcs) == 0: continue
        particle_words: List[str] = []
        for src in chunk.srcs:
          src_chunk = sentence[src]
          particle_morphs = [morph for morph in src_chunk.morphs if morph.pos == '助詞']
          if len(particle_morphs) == 0: continue
          particle_words.extend([morph.surface for morph in particle_morphs])
        particle_text = ' '.join(particle_words)
      
        print(f'{verb_morphs[0].base}\t{particle_text}', file=f)

if __name__ == '__main__':
  main_45()