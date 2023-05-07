import os
import torch
import torch.nn as nn
import torch.utils.data as data
from tqdm import tqdm
import time

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

def main_77():
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

  # モデルの定義
  model = SingleLayerNeuralNet(300, 4)
  model.train()

  # 損失関数の定義
  criterion = nn.CrossEntropyLoss()

  # 最適化手法の定義
  optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

  # 学習用の関数を定義
  def train_model(model, dataloaders_dict, criterion, optimizer, num_epochs):
    start_time = time.time()

    # epochのループ
    for epoch in range(num_epochs):
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
        
        print('{} Loss: {:.4f}, Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

    print(f'batch_size: {batch_size}')

    end_time = time.time()
    print(f'calc_time: {end_time - start_time}')
    
  # 学習を実行する
  num_epochs = 1

  # DataLoaderを作成
  batch_sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

  for batch_size in batch_sizes:
    train_dataloader = data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    valid_dataloader = data.DataLoader(valid_dataset, batch_size=len(valid_dataset), shuffle=False)
    test_dataloader = data.DataLoader(test_dataset, batch_size=len(test_dataset), shuffle=False)
    dataloaders_dict = {'train': train_dataloader, 'val': valid_dataloader, 'test': test_dataloader}
    train_model(model, dataloaders_dict, criterion, optimizer, num_epochs=num_epochs)

if __name__ == '__main__':
  main_77()