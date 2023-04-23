import os

def main_65():
  current_path = os.path.dirname(os.path.abspath(__file__))

  with open(f'{current_path}/../../text/result_64.txt') as f:
    len_semantic = 0
    len_grammatical = 0
    len_semantic_correct = 0
    len_grammatical_correct = 0

    for line in f:
      data = line.rstrip().split('\t')
      if data[0].startswith('gram'):
        len_grammatical += 1
        if data[1].split()[-1] == data[2]:
          len_grammatical_correct += 1
      else:
        len_semantic += 1
        if data[1].split()[-1] == data[2]:
          len_semantic_correct += 1

    print(f'意味的アナロジーの正解率: {len_semantic_correct / len_semantic}')
    print(f'文法的アナロジーの正解率: {len_grammatical_correct / len_grammatical}')

if __name__ == '__main__':
  main_65()