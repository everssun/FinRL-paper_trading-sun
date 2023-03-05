from paper_trading_1 import build_mlp
from unittest.mock import patch
#import gym
import torch
import torch.nn as nn
from torch import Tensor
from torch.nn import Sequential


def test_hello():
    assert build_mlp([8, 1, 2]) == Sequential(
  (0): Linear(in_features=8, out_features=1, bias=True)
  (1): ReLU()
  (2): Linear(in_features=1, out_features=2, bias=True)
)


@patch('builtins.print')
def test_print_hello(mock_print):
    build_mlp([8, 1, 2])
    assert mock_print.call_args.args == (Sequential(
  (0): Linear(in_features=8, out_features=1, bias=True)
  (1): ReLU()
  (2): Linear(in_features=1, out_features=2, bias=True)
),)