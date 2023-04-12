from graphviz import Digraph
from No_41 import main_41

def main_44():
  g = Digraph()

  sentences = main_41()
  for chunk in sentences[1]:
    if chunk.dst == -1:
      continue
    morphs_text = ''.join([morph.surface for morph in chunk.morphs if morph.pos != '記号' ])
    dst_chunk = sentences[1][chunk.dst]
    dst_text = ''.join([morph.surface for morph in dst_chunk.morphs if morph.pos != '記号' ])
    g.edge(morphs_text, dst_text)
  
  g.view()

if __name__ == '__main__':
  main_44()
