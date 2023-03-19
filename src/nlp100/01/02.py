
if __name__ == '__main__':
  string1 = 'パトカー'
  string2 = 'タクシー'
  answer = ''.join([i + j for i, j in zip(string1, string2)])
  print(answer)