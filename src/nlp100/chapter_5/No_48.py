from No_41 import main_41
import os

def main_48():
  current_path = os.path.dirname(os.path.abspath(__file__))

  sentences = main_41()
  
  with open(f'{current_path}/../../text/result_48.txt', 'w') as f:
    for sentence in sentences:
      for chunk in sentence:
        pos_list = [morph.pos for morph in chunk.morphs]

        if '名詞' in pos_list:
          path = [''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号'])]

          next_chunk_index = chunk.dst

          while next_chunk_index != -1:
            path.append(''.join([morph.surface for morph in sentence[next_chunk_index].morphs if morph.pos != '記号']))
            
            next_chunk_index = sentence[next_chunk_index].dst

          print('->'.join(path), file=f)

if __name__ == '__main__':
  main_48()