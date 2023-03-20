import os

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))
  
  col1 = open(f'{path}/../../text/col1.txt', 'w')
  col2 = open(f'{path}/../../text/col2.txt', 'w')

  with open(f'{path}/../../text/popular-names.txt') as f:
    for line in f:
      line_list = line.split('\t')
      col1.write(f'{line_list[0]}\n')
      col2.write(f'{line_list[1]}\n')

  col1.close()
  col2.close()

