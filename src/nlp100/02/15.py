import os

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))
  n = int(input())

  f = open(f'{path}/../../text/popular-names.txt')
  data = f.readlines()

  for line in data[-n:]:
    print(line)
  
  f.close()
