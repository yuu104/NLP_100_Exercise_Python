import os
import re
from typing import Union

def main_25() -> Union[dict[str, str], None]:
  path = os.path.dirname(os.path.abspath(__file__))

  f = open(f'{path}/../../text/country-uk.txt')
  data = f.read()
  f.close()
  
  pattern = '\\{\\{基礎情報[\\s\\S]*?\n\\}\\}'
  res = re.search(pattern, data)

  if res:
    basic_info = res.group()
    item_pattern = '\\|(.*)=(.*)\n'
    items = re.findall(item_pattern, basic_info)
    
    dic: dict[str, str] = {}
    for item in items:
      dic[item[0].strip()] = item[1].strip()
    
    return dic
  else:
    return None

if __name__ == '__main__':
  print(main_25())