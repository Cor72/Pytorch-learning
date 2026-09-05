import torch
w=torch.tensor(10,requires_grad=True,dtype=float)

loss=2*w**2
loss.sum().backward()

w.data-=0.01*w.grad.data

print(f'{w}')