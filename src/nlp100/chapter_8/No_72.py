import os
import torch
import torch.nn as nn

class SingleLayerNeuralNet(nn.Module):
  def __init__(self, input_dim: int, output_dim: int):
    super(SingleLayerNeuralNet, self).__init__()
    self.liner = nn.Linear(input_dim, output_dim)

  def forward(self, x):
    out = self.liner(x)
    return out

def main_72():
  current_path = os.path.dirname(os.path.abspath(__file__))

  model = SingleLayerNeuralNet(300, 4)

  X_train = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/X_train.pt')
  y_train = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/y_train.pt')

  criterion = nn.CrossEntropyLoss()

  output_X1 = model(X_train[0])
  loss_X1 = criterion(output_X1, y_train[0])
  model.zero_grad()
  loss_X1.backward()
  grads_X1 = model.liner.weight.grad
  print('損失：', loss_X1)
  print('勾配：', grads_X1)

  output_X1_4 = model(X_train[:4])
  loss_X1_4 = criterion(output_X1_4, y_train[:4])
  model.zero_grad()
  loss_X1_4.backward()
  grads_X1_4 = model.liner.weight.grad
  print('損失', loss_X1_4)
  print('勾配', grads_X1_4)

if __name__ == '__main__':
  main_72()