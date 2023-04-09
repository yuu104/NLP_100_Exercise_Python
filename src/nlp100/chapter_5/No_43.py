from No_41 import main_41

def main_43():
  sentences = main_41()
  for chunk in sentences[1]:
    if chunk.dst == -1:
      continue

    dst_chunk = sentences[1][chunk.dst]
    if any(morph.pos == '名詞' for morph in chunk.morphs) and any(morph.pos == '動詞' for morph in dst_chunk.morphs):
      morphs_text = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号' ])
      dst_text = ''.join([morph.surface for morph in dst_chunk.morphs if morph.pos != '記号' ])
      print(f'{morphs_text}\t{dst_text}')

if __name__ == '__main__':
  main_43()