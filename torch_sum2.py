import torch

w=torch.tensor(10,requires_grad=True,dtype=float)
loss=w**2+20
loss.sum().backward()
