import os
import re
from typing import List

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))

  f = open(f'{path}/../../text/country-uk.txt')
  data = f.read()
  
  pattern = '\\{\\{基礎情報[\\s\\S]*?\n\\}\\}'
  res = re.search(pattern, data)

  if res:
    basic_info = res.group()
    item_pattern = '\\|(.*)=(.*)\n'
    items: List[str] = re.findall(item_pattern, basic_info)
    
    dic = {}
    for item in items:
      dic[item[0].strip()] = item[1].strip()
    
    print(dic)

  f.close()