import os
from typing import List
from No_41 import main_41

def main_46():
  current_path = os.path.dirname(os.path.abspath(__file__))
  sentences = main_41()
  
  with open(f'{current_path}/../../text/result_46.txt', 'w') as f:
    for sentence in sentences:
      for chunk in sentence:
        verb_morphs = [morph for morph in chunk.morphs if morph.pos == '動詞']
        if len(verb_morphs) == 0 or len(chunk.srcs) == 0: continue
        particle_words: List[str] = []
        particle_phrases: List[str] = []
        for src in chunk.srcs:
          src_chunk = sentence[src]
          particle_morphs = [morph for morph in src_chunk.morphs if morph.pos == '助詞']
          if len(particle_morphs) == 0: continue
          particle_phrase_list = [morph.surface for morph in src_chunk.morphs]
          particle_phrase = ''.join(particle_phrase_list)
          particle_phrases.append(particle_phrase)
          particle_words.extend([morph.surface for morph in particle_morphs])
        particle_text = ' '.join(particle_words)
        particle_phrases_text = ' '.join(particle_phrases)
      
        print(f'{verb_morphs[0].base}\t{particle_text}\t{particle_phrases_text}', file=f)

if __name__ == '__main__':
  main_46()