import os
from typing import List
from No_40 import Morph

class Chunk:
  def __init__(self, morphs: List[Morph], dst: int, srcs: List[int]) -> None:
    self.morphs = morphs
    self.dst = dst
    self.srcs = srcs

def main_41() -> List[List[Chunk]]:
  current_path = os.path.dirname(os.path.abspath(__file__))
  
  sentence: List[List[Chunk]] = []
  
  with open(f'{current_path}/../../parsed/ai.ja.txt.parsed') as f:
    dst = 0
    chunks: List[Chunk] = []
    morphs: List[Morph] = []
    for line in f:
      if line[0] == '*':
        if len(morphs):
          chunk = Chunk(morphs, dst, srcs=[])
          chunks.append(chunk)
          morphs = []
        dst = int(line.split()[2].rstrip('D'))
      elif line == 'EOS\n':
        if len(chunks) or len(morphs):
          chunk = Chunk(morphs, dst, srcs=[])
          chunks.append(chunk)
          morphs = []
          sentence.append(chunks)
          for index, item in enumerate(chunks):
            if (item.dst == -1):
              continue
            chunks[item.dst].srcs.append(index)
          chunks = []
      else:
        morph = Morph(line)
        morphs.append(morph)
  
  return sentence

if __name__ == '__main__':
  sentence = main_41()
  for item in sentence[1]:
    print(vars(item))

# ai.ja.txt.parsed を一行づつ見ていく
# lie[0] == '*' だったら、Chunkのインスタンスを作成する
  # dst = line[1], srcs = []
# 各形態素に対してMorphのインスタンスを作成し、morphsリストに追加する
# line == 'EOS\n'の場合
  # len(morphs) != 0 の場合
    # Chunkのインスタンスのmorphsにmorphsを代入する
    # morphs = []
  # else
    # sentenceに追加する