import os
import torch
import torch.utils.data as data
from No_73 import SingleLayerNeuralNet, NewsDataset

def calc_acc(model, dataloader):
  model.eval()
  corrects = 0
  with torch.no_grad():
    for inputs, labels in dataloader:
      outputs = model(inputs)
      _, preds = torch.max(outputs, 1) # ラベルを予測
      corrects += torch.sum(preds == labels.data)
  return corrects / len(dataloader.dataset)

def main_74():
  current_path = os.path.dirname(os.path.abspath(__file__))

  X_train = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/X_train.pt')
  y_train = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/y_train.pt')
  X_valid = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/X_valid.pt')
  y_valid = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/y_valid.pt')
  X_test = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/X_test.pt')
  y_test = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/y_test.pt')

  train_dataset = NewsDataset(X_train, y_train, phase='train')
  valid_dataset = NewsDataset(X_valid, y_valid, phase='val')
  test_dataset = NewsDataset(X_test, y_test, phase='val')

  model = SingleLayerNeuralNet(300, 4)

  # DataLoaderを作成
  batch_size = 1
  train_dataloader = data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
  valid_dataloader = data.DataLoader(valid_dataset, batch_size=len(valid_dataset), shuffle=False)
  test_dataloader = data.DataLoader(test_dataset, batch_size=len(test_dataset), shuffle=False)
  
  acc_train = calc_acc(model, train_dataloader)
  acc_valid = calc_acc(model, valid_dataloader)
  acc_test = calc_acc(model, test_dataloader)
  print('学習データの正解率: {:.4f}'.format(acc_train))
  print('検証データの正解率: {:.4f}'.format(acc_valid))
  print('テストデータの正解率: {:.4f}'.format(acc_test))

if __name__ == '__main__':
  main_74()