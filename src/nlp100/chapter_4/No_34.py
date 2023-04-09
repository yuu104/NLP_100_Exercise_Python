from .No_30 import main_30
from pprint import pprint
from typing import List

def main_34() -> List[str]:
  morphemic_sentences = main_30()
  pprint(morphemic_sentences[:5])
  
  ans: List[str] = []
  max_count = 0
  for sentence in morphemic_sentences:
    count = 0
    conjunction_nouns = ''
    for index, morpheme in enumerate(sentence):
      if morpheme['pos'] == '名詞':
        count += 1
        conjunction_nouns += morpheme['base']
        if index == len(sentence) - 1:
          max_count = check_count(count, max_count, ans, conjunction_nouns)
          count = 0
          conjunction_nouns = ''
      else:
        max_count = check_count(count, max_count, ans, conjunction_nouns)
        count = 0
        conjunction_nouns = ''
  return ans

def check_count(count: int, max_count: int, ans: List[str], conjunction_nouns: str) -> int:
  if count != 0 and count > max_count:
    max_count = count
    ans.clear()
    ans.append(conjunction_nouns)
  elif count != 0 and count == max_count:
    ans.append(conjunction_nouns)
  return max_count

if __name__ == '__main__':
  conjunction_nouns_list = main_34() 
  print(conjunction_nouns_list)

# やること
# 1. morphemic_sentences をfor文で順番に見る
# 2. morphemic_sentence　の各形態素を順番に見る
# 3. 形態素が「名詞」であればカウント開始
# 4. 次の形態素が「名詞」であればカウント
# 5. 次の形態素が「名詞」でなければカウント終了
# 6. カウントが最長であれば ans の要素をクリアし、ans に格納
# 7. カウントが max_count と同じであれば、そのまま ans に格納
# 8. 次の形態素を確認して、3〜7を繰り返す
# 9. sentence の最後の行が「名詞」であれば6〜7を実行する