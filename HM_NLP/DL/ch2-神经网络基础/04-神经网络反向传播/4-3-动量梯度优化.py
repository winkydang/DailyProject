import torch

def test():

    # 1 初始化权重参数
    w = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)
    y = (w ** 2) / 2.0
    z = y.sum()

    # 2 实例化优化方法：SGD 指定参数beta=0.9
    optimizer = torch.optim.SGD([w], lr=0.01, momentum=0.9)

    # 3 第1次更新 计算梯度，并对参数进行更新
    optimizer.zero_grad()
    z.backward()
    optimizer.step()

    print('第1次: 梯度w.grad: %.10f, 更新后的权重:%.10f' %(w.grad.numpy(), w.detach().numpy()) )

    # 4 第2次更新 计算梯度，并对参数进行更新
    y = (w ** 2) / 2.0
    z = y.sum()

    optimizer.zero_grad()
    z.backward()
    optimizer.step()
    print('第2次: 梯度w.grad: %.10f, 更新后的权重:%.10f' % (w.grad.numpy(), w.detach().numpy()) )

test()

