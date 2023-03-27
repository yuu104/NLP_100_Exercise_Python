import os
import re

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))

  f = open(f'{path}/../../text/country-uk.txt')
  data = f.read()

  pattern = r'\[\[ファイル:(.*?)[\|\]]'
  files = re.findall(pattern, data)
  
  for file in files:
    print(file)

  f.close()