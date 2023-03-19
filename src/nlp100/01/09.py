import random
from typing import List

if __name__ == '__main__':
  text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

  answer_list: List[str] = []
  for word in text.split():
    if len(word) > 4:
      word_list = list(word)
      random.shuffle(word_list)
      answer_list.append(''.join(word_list))
    else:
      answer_list.append(word)
  
  print(' '.join(answer_list))
