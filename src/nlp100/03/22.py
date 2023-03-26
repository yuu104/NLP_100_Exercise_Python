import os
import re

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))
  f = open(f'{path}/../../text/country-uk.txt')
  data = f.read()
  
  pattern = r'\[\[Category:(.*)\]\]'
  res = re.findall(pattern, data)
  for category_name in res:
    print(category_name)
  
  f.close()