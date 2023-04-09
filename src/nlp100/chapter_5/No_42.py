from .No_41 import main_41

def main_42():
  sentences = main_41()
  for chunk in sentences[1]:
    if chunk.dst == -1:
      continue
    morphs_text = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号' ])
    dst_chunk = sentences[1][chunk.dst]
    dst_text = ''.join([morph.surface for morph in dst_chunk.morphs if morph.pos != '記号' ])
    print(f'{morphs_text}\t{dst_text}')

if __name__ == '__main__':
  main_42()