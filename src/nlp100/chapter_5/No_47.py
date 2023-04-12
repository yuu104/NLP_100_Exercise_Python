import os
from typing import List
from No_41 import main_41

def main_47():
  current_path = os.path.dirname(os.path.abspath(__file__))
  sentences = main_41()
  
  with open(f'{current_path}/../../text/result_47.txt', 'w') as f:
    for sentence in sentences:
      for chunk in sentence:
        for morph in chunk.morphs:
          if morph.pos == '動詞': # 動詞を含む文節を見つける
            predicates = ''
            particle_words = []
            particle_chunk_words = []
            for src in chunk.srcs: # 動詞を含む文節に係る文節を順番に見ていく
              svc_morphs = [[morph, index] for index, morph in enumerate(sentence[src].morphs) if morph.pos1 == 'サ変接続'] # サ変接続の名詞を検索
              if len(svc_morphs):
                svc_morph = svc_morphs[0]
                if len(sentence[src].morphs) - 1 != svc_morph[1] and sentence[src].morphs[svc_morph[1] + 1].base == 'を':
                  predicates = ''.join([svc_morph[0].surface, 'を', morph.base])
                  continue
              particle_base_list = [morph.base for morph in sentence[src].morphs if morph.pos == '助詞'] # 助詞を検索
              if len(particle_base_list) == 0: continue
              particle_words.extend(particle_base_list)
              particle_chunk_words.append(''.join([morph.surface for morph in sentence[src].morphs]))

            if predicates != '': # 述語が存在すれば出力する
              particle_words_text = ' '.join(particle_words)
              particle_chunk_words_text = ' '.join(particle_chunk_words)
              print(f'{predicates}\t{particle_words_text}\t{particle_chunk_words_text}')


if __name__ == '__main__':
  main_47()