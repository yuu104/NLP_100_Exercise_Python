import re

if __name__ == '__main__':
  text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can'
  cleaned_text = re.sub(r'[^\w\s]', '', text)
  cleaned_text_array = cleaned_text.split()
  
  one_word_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
  
  ans = {}

  for index, word in enumerate(cleaned_text_array):
    if index + 1 in one_word_index:
      ans[word[:1]] = index + 1
    else:
      ans[word[:2]] = index + 1
  
  print(ans)

