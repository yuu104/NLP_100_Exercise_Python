def cipher(text: str) -> str:
  text_list = []
  for char in text:
    if char.islower():
      text_list.append(chr(219 - ord(char)))
    else:
      text_list.append(char)
  return ''.join(text_list)

if __name__ == '__main__':
  text = 'Hello World'
  encrypted_text = cipher(text)
  decrypted_text = cipher(encrypted_text)

  print(f'暗号化: {encrypted_text}')
  print(f'復号化: {decrypted_text}')
