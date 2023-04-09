from .No_30 import main_30
from pprint import pprint
from typing import List

def main_33():
  morphemic_sentence = main_30()
  
  noun_phrase = []
  for sentence in morphemic_sentence:
    for index in range(len(sentence)):
      if len(sentence) < 3 or index == len(sentence) - 2:
        break

      first_morpheme = sentence[index]
      second_morpheme = sentence[index + 1]
      third_morpheme = sentence[index + 2]

      if first_morpheme['pos'] == '名詞' and second_morpheme['base'] == 'の' and third_morpheme['pos'] == '名詞':
        noun_phrase.append(first_morpheme['base'] + second_morpheme['base'] + third_morpheme['base'])
        
  print(noun_phrase)

if __name__ == '__main__':
  main_33()

