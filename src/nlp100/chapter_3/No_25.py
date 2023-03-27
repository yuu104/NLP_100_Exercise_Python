import os
import re

def main_25():
  path = os.path.dirname(os.path.abspath(__file__))

  f = open(f'{path}/../../text/country-uk.txt')
  data = f.read()
  
  pattern = '\\{\\{基礎情報[\\s\\S]*?\n\\}\\}'
  res = re.search(pattern, data)

  if res:
    basic_info = res.group()
    item_pattern = '\\|(.*)=(.*)\n'
    items = re.findall(item_pattern, basic_info)
    
    dic = {}
    for item in items:
      dic[item[0].strip()] = item[1].strip()
    
    return dic

  f.close()

if __name__ == '__main__':
  print(main_25())