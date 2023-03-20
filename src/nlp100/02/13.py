import os

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))

  col1 = open(f'{path}/../../text/col1.txt')
  col1_data = col1.read().splitlines()
  col2 = open(f'{path}/../../text/col2.txt')
  col2_data = col2.read().splitlines()

  with open(f'{path}/../../text/marge.txt', 'w') as f:
    for i in range(len(col1_data)):
      f.write(f'{col1_data[i]}\t{col2_data[i]}\n')
    
  col1.close()
  col2.close()
