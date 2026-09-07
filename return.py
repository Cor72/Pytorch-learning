import torch
from torch.utils.data import DataLoader
from torch.utils.data import TensorDataset
from torch import nn
from torch import optim
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def create_dataset():
    x, y, coef = make_regression(
        n_samples=100,
        n_features=1,
        n_informative=1,
        noise=10,
        coef=True,
        random_state=3
    )
    print(coef)
    print(type(x))
    return x, y, coef


if __name__ == '__main__':
    create_dataset()