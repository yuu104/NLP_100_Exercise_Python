import os

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))
  n = int(input())

  with open(f'{path}/../../text/popular-names.txt') as f:
    for index, line in enumerate(f):
      if index < n:
        print(line)
      else:
        break
