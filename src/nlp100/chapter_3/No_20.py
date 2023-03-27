import json
import os
from typing import TypedDict, List

class CountryWiki(TypedDict):
  title: str
  text: str

if __name__ == '__main__':
  path = os.path.dirname(os.path.abspath(__file__))

  data: List[CountryWiki] = []
  with open(f'{path}/../../json/jawiki-country.json') as f:
    for line in f:
      data.append(json.loads(line))
  
  for country in data:
    if country['title'] == 'イギリス':
      with open(f'{path}/../../text/country-uk.txt', 'w') as country_uk_f:
        country_uk_f.write(country['text'])
      break

