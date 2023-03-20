import os

if __name__ == '__main__':
  path = os.getcwd()

  f = open(f'{path}/src/text/popular-names.txt')
  data = f.readlines()
  f.close()

  print(len(data))

