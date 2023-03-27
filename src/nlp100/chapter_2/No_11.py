import os

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))
  
  with open(f'{path}/../../text/popular-names.txt') as f:
    for line in f:
      line.replace('\t', ' ')
      print(line)
