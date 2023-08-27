"""
神经网络的训练有时需要几天、几周、甚至几个月，为了在每次使用模型时避免高代价的重复训练，我们就需要将模型序列化到磁盘中，使用的时候反序列化到内存中。

PyTorch 提供了两种保存模型的方法：
    1. 直接序列化模型对象
    2. 存储模型的网络参数.把模型的一些初始化参数、模型的权重参数、训练的迭代次数、以及优化器的参数等都进行了存储。

本小节主要带着学习了如何保存网络模型。我们可以直接存储模型对象，但是该方法依赖于 PyTorch 的实现，
而存储模型参数与 PyTorch 的实现关系较弱，建议使用第二种方法来存储模型。

"""
import os.path
from settings import cur_path

# # 方式一： 直接序列化模型对象
# import torch
# from torch import nn
# import pickle
#
#
# # 创建模型类,继承Module类(模型构造类,是所有神经网络模块的父类)
# class Model(nn.Module):
#     # 初始化属性
#     def __init__(self, input_size, output_size):
#         # 调用父类的初始化属性
#         super(Model, self).__init__()
#         # 创建隐藏层
#         self.linear1 = nn.Linear(input_size, input_size * 2)
#         self.linear2 = nn.Linear(input_size * 2, output_size)
#
#     # 定义模型的前向传播计算,即如何根据输入x计算返回所需要的模型输出
#     def forward(self, inputs):
#         inputs = self.linear1(inputs)
#         output = self.linear2(inputs)
#         return output
#
#
# # 保存模型
# def test01():
#     # 构造模型
#     model = Model(128, 10)
#     # 保存模型
#     # 第一个参数obj:存储的模型对象
#     # 第二个参数path:存在的路径,模型文件是.pt或.pth格式
#     # 第三个参数pickle_module:使用的模块
#     # 第四个参数pickle_protocol:存储的协议.使用的协议越高，读取生成的pickle所需的Python版本越新。
#     torch.save(model, os.path.join(cur_path, "HM_NLP/DL/model/test_model_save.pth"), pickle_module=pickle, pickle_protocol=2)
#     # Python 的 Pickle 序列化协议有多种，详细可查看官网: https://www.python.org/search/?q=pickle+protocol
#
#
# # 加载模型
# def test02():
#     # 第一个参数path: 加载的模型路径
#     # 第二个参数map_location: 模型加载的设备
#     # 第三个参数pickle_module: 加载的模块
#     model = torch.load(os.path.join(cur_path, "HM_NLP/DL/model/test_model_save.pth"), map_location="cpu", pickle_module=pickle)
#     return model
# # 注意: 当我们训练的模型在 GPU 中时，torch.save 函数将其存储到磁盘中。当再次加载该模型时，会将该模型从磁盘先加载到 CPU 中，再移动到指定的 GPU 中，例如： cuda:0、cuda:1。但是，当重新加载的机器不存在 GPU 时，模型加载可能会出错，这时，可通过 map_localtion=’CPU’ 将其加载到 CPU 中。
#
# if __name__ == '__main__':
#     test01()
#     model = test02()
#     # Model(
#     # (linear1): Linear(in_features=128, out_features=256, bias=True)
#     #  (linear2): Linear(in_features=256, out_features=10, bias=True)
#     # )
#     print(model.parameters())  # <generator object Module.parameters at 0x161b59dd0>
#     print(model.parameters)
#     # <bound method Module.parameters of Model(
#     # (linear1): Linear(in_features=128, out_features=256, bias=True)
#     #  (linear2): Linear(in_features=256, out_features=10, bias=True)
#     # )>
#     print(model.linear1)  # Linear(in_features=128, out_features=256, bias=True)
#     print(model.linear2)  # Linear(in_features=256, out_features=10, bias=True)


# 方式二： 存储模型的网络参数

import torch
from torch import nn
from torch import optim


# 创建模型类,继承Module类(模型构造类,是所有神经网络模块的父类)
class Model(nn.Module):
    # 初始化属性
    def __init__(self, input_size, output_size):
        # 调用父类的初始化属性
        super(Model, self).__init__()
        # 创建隐藏层
        self.linear1 = nn.Linear(input_size, input_size * 2)
        self.linear2 = nn.Linear(input_size * 2, output_size)

    # 定义模型的前向计算,即如何根据输入x计算返回所需要的模型输出
    def forward(self, inputs):
        inputs = self.linear1(inputs)
        output = self.linear2(inputs)
        return output


# 保存模型参数
def test01():
    # 构造模型
    model = Model(128, 10)
    print(model.state_dict())
    # OrderedDict([('linear1.weight', tensor([[ 0.0837, -0.0201, -0.0074,  ...,  0.0410, -0.0342, -0.0253],
        # ...,[ 0.0761,  0.0277, -0.0835,  ..., -0.0417, -0.0308,  0.0242]])),
        # ('linear1.bias', tensor([ 6.9128e-02, -8.4044e-02, -2.1395e-02, -1.6658e-02,  1.5486e-02,
        # ...-4.3652e-02,-5.0783e-03])),
        # ('linear2.weight', tensor([[ 1.0431e-06,  2.9279e-02,  1.9844e-02,  ..., -2.5576e-02,5.2676e-02, -6.0955e-02],...,[ 5.2701e-02,  2.0256e-03,  3.1913e-02,  ...,  5.4276e-02,
        #  -4.2626e-02,  3.3084e-02]])),
        #  ('linear2.bias', tensor([-0.0515, -0.0215,  0.0611, -0.0399, -0.0030,  0.0099,  0.0426, -0.0505,
        #  0.0214,  0.0317]))])
    # 构造优化函数
    optimizer = optim.Adam(params=model.parameters(), lr=1e-3)
    print(optimizer.state_dict())  # {'state': {}, 'param_groups': [{'lr': 0.001, 'betas': (0.9, 0.999), 'eps': 1e-08, 'weight_decay': 0, 'amsgrad': False, 'maximize': False, 'foreach': None, 'capturable': False, 'differentiable': False, 'fused': None, 'params': [0, 1, 2, 3]}]}

    # 定义存储参数
    save_params = {
        "init_params": {
            "input_size": 128,
            "output_size": 10
        },
        "acc_score": 0.98,  # 准确率
        "avg_loss": 0.86,  # 平均损失值
        "iter_numbers": 100,  # 迭代次数
        'optim_params': optimizer.state_dict(),  # 提取优化器参数
        'model_params': model.state_dict()  # 提取模型参数
    }

    # 存储模型参数
    torch.save(save_params, os.path.join(cur_path, "HM_NLP/DL/model/test_model_save_2.pth"))


# 根据模型参数初始化模型和优化器
def test02():
    # 加载模型参数
    model_params = torch.load(os.path.join(cur_path, "HM_NLP/DL/model/test_model_save_2.pth"))
    print("model_params-->", model_params)
    # 初始化模型
    model = Model(model_params['init_params']['input_size'], model_params['init_params']['output_size'])          # model_params['init_params']['input_size']: 128, model_params['init_params']['output_size']:10
    # 初始化优化器
    optimizer = optim.Adam(model.parameters())
    # 加载优化器参数
    optimizer.load_state_dict(model_params["optim_params"])  # model_params["optim_params"]: {'state': {}, 'param_groups': [{'lr': 0.001, 'betas': (0.9, 0.999), 'eps': 1e-08, 'weight_decay': 0, 'amsgrad': False, 'maximize': False, 'foreach': None, 'capturable': False, 'differentiable': False, 'fused': None, 'params': [0, 1, 2, 3]}]}

    # 显示其他参数
    print('迭代次数:', model_params['iter_numbers'])
    print('准确率:', model_params['acc_score'])
    print('平均损失:', model_params['avg_loss'])


if __name__ == '__main__':
    test01()
    test02()










