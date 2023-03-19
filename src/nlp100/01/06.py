from typing import Set

def ngram(n:int, text: str) -> Set[str]:
  ngram_set: Set[str] = set()
  for index in range(len(text1) - n + 1):
    ngram_set.add(text[index:index + n])
  
  return ngram_set

if __name__ == '__main__':
  text1 = 'paraparaparadise'
  text2 = 'paragraph'

  x = ngram(2, text1)
  y = ngram(2, text2)

  print(f'X: {x}')
  print(f'Y: {y}')
  print(f'和集合: {x | y}')
  print(f'積集合: {x & y}')
  print(f'差集合: {x - y}')

  if 'se' in x:
    print('se は X に含まれます')
  else:
    print('se は X に含まれません')
  
  if 'se' in y:
    print('se は Y に含まれます')
  else:
    print('se は Y に含まれません')
