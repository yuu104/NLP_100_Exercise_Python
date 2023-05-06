import os
import torch
import torch.nn as nn
import numpy as np

class SingleLayerNeuralNet(nn.Module):
  def __init__(self, input_dim: int, output_dim: int):
    super(SingleLayerNeuralNet, self).__init__()
    self.liner = nn.Linear(input_dim, output_dim)

  def forward(self, x):
    out = self.liner(x)
    return out
  
def main_71():
  current_path = os.path.dirname(os.path.abspath(__file__))

  model = SingleLayerNeuralNet(300, 4)
  
  X_train = torch.load(f'{current_path}/../../NewsAggregatorDataset/chapter_8/X_train.pt')

  X1_outputs = model(X_train[0])
  y_hat_1 = nn.Softmax(dim=-1)(X1_outputs)

  X1_4_outputs = model(X_train[:4])
  y_hat = nn.Softmax(dim=1)(X1_4_outputs)

  print(y_hat_1)
  print(y_hat)

if __name__ == '__main__':
  main_71()