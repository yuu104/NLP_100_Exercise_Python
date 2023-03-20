import os

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))
  n = int(input())

  f = open(f'{path}/../../text/popular-names.txt')
  data = f.readlines()

  num_of_divisions = len(data) // n + len(data) % n
  
  index = 0
  for i in range(n):
    with open(f'{path}/../../text/divisions/division{i}.txt', 'w') as division_file:
      division_file.writelines(data[i*num_of_divisions:(i+1)*num_of_divisions])
  
  f.close()

# 商 + 1 の数だけファイルを分割する
