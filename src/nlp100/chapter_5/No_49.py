from itertools import combinations
from typing import List, TypedDict
from No_41 import main_41, Chunk

class NounChunk(TypedDict):
  index: int
  chunk: Chunk

def main_49():
  sentences = main_41()

  i = 0
  for sentence in sentences:
    if i == 2: break
    i += 1

    noun_chunks: List[NounChunk] = [{'index': index, 'chunk': chunk} for index, chunk in enumerate(sentence) if '名詞' in [morph.pos for morph in chunk.morphs]]

    if len(noun_chunks) < 2 : continue

    noun_chunk_combi_list = list(combinations(noun_chunks, 2))

    for combi in noun_chunk_combi_list:
      noun_chunk_i = combi[0] if combi[0]['index'] < combi[1]['index'] else combi[1]

      noun_chunk_j = combi[1] if combi[0]['index'] < combi[1]['index'] else combi[0]

      next_chunk_index = noun_chunk_i['chunk'].dst

      is_same_route = False

      while next_chunk_index != -1:
        if next_chunk_index == noun_chunk_j['index']:
          is_same_route = True
          break

        next_chunk_index = sentence[next_chunk_index].dst
      
      if is_same_route:
        chunk_path_list: List[Chunk] = []

        is_noun = False
        for index, morph in enumerate(noun_chunk_i['chunk'].morphs):
          if morph.pos == '名詞':
            if is_noun == False:
              noun_chunk_i['chunk'].morphs[index].surface = 'x'
              is_noun = True
            else:
              noun_chunk_i['chunk'].morphs[index].surface = ''
        
        chunk_path_list.append(noun_chunk_i['chunk'])

        next_index = noun_chunk_i['chunk'].dst

        while next_index == noun_chunk_j['index']:
          chunk_path_list.append(sentence[next_index])

          next_index = sentence[next_index].dst

        path_string = '->'.join([''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号']) for chunk in chunk_path_list]) + '->y'
        print(path_string)

if __name__ == '__main__':
  main_49()