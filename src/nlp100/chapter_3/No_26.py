import os
import sys
import re
from No_25 import main_25

if __name__ == '__main__':
  basic_info = main_25()

  if not basic_info:
    sys.exit()
  
  for key in basic_info:
    res = re.search("('{2,5})(.*?)(\\1)", basic_info[key])
    if res:
      replaced_text = res.group().replace("'", '')
      basic_info[key] = replaced_text
      print(basic_info[key])
  
  print(basic_info)
