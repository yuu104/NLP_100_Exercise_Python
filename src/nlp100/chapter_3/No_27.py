import re
from pprint import pprint
from No_26 import main_26

def main_27() -> dict[str, str]:
  basic_info = main_26()

  for key in basic_info:
    basic_info[key] = re.sub(r'\[\[(.*)#(.*)\|(.*?)\]\]', r'\3', basic_info[key])
    basic_info[key] = re.sub(r'\[\[(.*)\|(.*?)\]\]', r'\2', basic_info[key])
    basic_info[key] = re.sub(r'\[\[(.*?)\]\]', r'\1', basic_info[key])
  
  return basic_info

if __name__ == '__main__':
  pprint(main_27(), sort_dicts=False)