from No_41 import main_41

def main_48():
  sentences = main_41()
  for chunk in sentences[1]:

    pos_list = [morph.pos for morph in chunk.morphs]
    if '名詞' in pos_list:
      path = [''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])]
      next_chunk_index = chunk.dst
      while next_chunk_index != -1:
        path.append(''.join([morph.surface for morph in sentences[1][next_chunk_index].morphs if morph.pos != '記号']))
        next_chunk_index = sentences[1][next_chunk_index].dst
      print('->'.join(path))

if __name__ == '__main__':
  main_48()