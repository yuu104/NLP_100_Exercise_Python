import os
import torch
import torch.nn as nn
import torch.utils.data as data
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt

# データセットを作成する
class NewsDataset(data.Dataset):
  def __init__(self, X, y, phase='train') -> None:
    self.X = X
    self.y = y
    self.phase = phase
  
  def __len__(self):
    return len(self.y)

  def __getitem__(self, idx):
    return self.X[idx], self.y[idx]

class SingleLayerNeuralNet(nn.Module):
  def __init__(self, input_dim: int, output_dim: int):
    super(SingleLayerNeuralNet, self).__init__()
    self.liner = nn.Linear(input_dim, output_dim)

  def forward(self, x):
    out = self.liner(x)
    return out

def main_75_76():
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
  
  # DataLoaderを作成
  batch_size = 1
  train_dataloader = data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
  valid_dataloader = data.DataLoader(valid_dataset, batch_size=len(valid_dataset), shuffle=False)
  test_dataloader = data.DataLoader(test_dataset, batch_size=len(test_dataset), shuffle=False)
  dataloaders_dict = {'train': train_dataloader, 'val': valid_dataloader, 'test': test_dataloader}

  # モデルの定義
  model = SingleLayerNeuralNet(300, 4)
  model.train()

  # 損失関数の定義
  criterion = nn.CrossEntropyLoss()

  # 最適化手法の定義
  optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

  # 学習用の関数を定義
  def train_model(model, dataloaders_dict, criterion, optimizer, num_epochs):
    train_loss = []
    train_acc = []
    valid_loss = []
    valid_acc = []

    # epochのループ
    for epoch in range(num_epochs):
      print(f'Epoch {epoch + 1} / {num_epochs}')
      print('--------------------------------------------')

      # epochごとの学習と検証のループ
      for phase in ['train', 'val']:
        if phase == 'train':
          model.train() # 訓練モード
        else:
          model.eval() # 検証モード
        
        epoch_loss = 0.0 # epochの損失和
        epoch_corrects = 0 # epochの正解数

        # データローダーからミニバッチを取り出すループ
        for inputs, labels in tqdm(dataloaders_dict[phase]):
          optimizer.zero_grad() # optimizerを初期化

          # 順伝播計算(forward)
          with torch.set_grad_enabled(phase == 'train'):
            outputs = model(inputs)
            loss = criterion(outputs, labels) # 損失を計算
            _, preds = torch.max(outputs, 1) # ラベルを予想

            # 訓練時は逆伝播
            if phase == 'train':
              loss.backward()
              optimizer.step()
            
            # イテレーション結果の計算
            # lossの合計を更新
            epoch_loss += loss.item() * inputs.size(0)
            # 正解数の合計を更新
            epoch_corrects += torch.sum(preds == labels.data)

        # epochごとのlossと正解率の表示
        epoch_loss = epoch_loss / len(dataloaders_dict[phase].dataset)
        epoch_acc = epoch_corrects.double() / len(dataloaders_dict[phase].dataset)

        if phase == 'train':
          train_loss.append(epoch_loss)
          train_acc.append(epoch_acc)
        else:
          valid_loss.append(epoch_loss)
          valid_acc.append(epoch_acc)
        
        print('{} Loss: {:.4f}, Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

      # チェックポイントの保存
      torch.save({'epoch': epoch, 'model_state_dict': model.state_dict(), 'optimizer_state_dict': optimizer.state_dict()},f'{current_path}/../../NewsAggregatorDataset/chapter_8/checkpoint{epoch + 1}.pt')
      
    return train_loss, train_acc, valid_loss, valid_acc

  # 学習を実行する
  num_epochs = 10
  train_loss, train_acc, valid_loss, valid_acc = train_model(model, dataloaders_dict, criterion, optimizer, num_epochs=num_epochs)

  fig, ax = plt.subplots(1,2, figsize=(10, 5))
  epochs = np.arange(num_epochs)
  ax[0].plot(epochs, train_loss, label='train')
  ax[0].plot(epochs, valid_loss, label='valid')
  ax[0].set_title('loss')
  ax[0].set_xlabel('epoch')
  ax[0].set_ylabel('loss')
  ax[1].plot(epochs, train_acc, label='train')
  ax[1].plot(epochs, valid_acc, label='valid')
  ax[1].set_title('acc')
  ax[1].set_xlabel('epoch')
  ax[1].set_ylabel('acc')
  ax[0].legend(loc='best')
  ax[1].legend(loc='best')
  plt.tight_layout()
  plt.savefig('fig74.png')

if __name__ == '__main__':
  main_75_76()