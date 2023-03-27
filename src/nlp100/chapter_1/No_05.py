from typing import List

if __name__ == '__main__':
  text = 'I am an NLPer'
  text_list = text.split()

  word_list: List[List[str]] = []
  char_list: List[str] = []

  for index in range(len(text_list) - 1):
    word_list.append(text_list[index:index+2])
  
  for index in range(len(text) - 1):
    char_list.append(text[index:index+2])

  print(f"単語bi-gram : {word_list}")
  print(f"文字bi-gram : {char_list}")