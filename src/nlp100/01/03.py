import re

if __name__ == '__main__':
  text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
  cleaned_text = re.sub(r'[^\w\s]', '', text)
  cleaned_text_array = cleaned_text.split()
  answer = [len(i) for i in cleaned_text_array]
  print(answer)