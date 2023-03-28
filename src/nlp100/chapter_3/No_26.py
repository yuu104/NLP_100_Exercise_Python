import sys
import re
from pprint import pprint
from No_25 import main_25

def main_26() -> dict[str, str]:
  basic_info = main_25()

  if not basic_info:
    sys.exit()
  
  for key in basic_info:
    res = re.search("('{2,5})(.*?)(\\1)", basic_info[key])
    if res:
      replaced_text = res.group().replace("'", '')
      basic_info[key] = replaced_text
  
  return basic_info

if __name__ == '__main__':
  pprint(main_26(), sort_dicts=False)
