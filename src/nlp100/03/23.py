import os
import re
from typing import List

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))

  f = open(f'{path}/../../text/country-uk.txt')
  data = f.read()

  pattern = '=(=.*=)='
  res: List[str] = re.findall(pattern, data)

  for section in res:
    level_str = re.match('^=+', section)
    section_name = section.replace('=', '')
    if level_str:
      level = len(level_str.group())
      print(level, section_name)

  f.close()