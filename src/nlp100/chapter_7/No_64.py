import os
from gensim.models import KeyedVectors

def main_64():
  current_path = os.path.dirname(os.path.abspath(__file__))

  model = KeyedVectors.load_word2vec_format(f'{current_path}/../../GoogleNews/GoogleNews-vectors-negative300.bin.gz', binary=True)
  
  with open(f'{current_path}/../../text/questions-words.txt', 'r') as question_file, open(f'{current_path}/../../text/result_64.txt', 'w') as result_file:
    category_name = ''
    for line in question_file:
      if line.startswith(':'):
        category_name = line.split()[1].rstrip()
      else:
        words = line.rstrip().split()
        most_similar_word = model.most_similar(positive=[words[1], words[2]], negative=[words[0]], topn=1)[0]
        result_file.write(f'{category_name}\t{line.rstrip()}\t{most_similar_word[0]}\t{most_similar_word[1]}\n')


if __name__ == '__main__':
  main_64()