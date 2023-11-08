# 参考：https://github.com/nicknochnack/OpenAI-Reinforcement-Learning-with-Custom-Environment/blob/main/OpenAI%20Custom%20Environment%20Reinforcement%20Learning.ipynb
# !pip install tensorflow==2.3.0
# !pip install gym
# !pip install keras
# !pip install keras-rl2
from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random


# 这段代码主要是定义和实现了一个基于OpenAI Gym的简单环境，模拟了一个调节淋浴水温的场景。
# 在这个环境中，代理可以采取三种行动（上，下，保持不变）来尝试保持水温在一个合适的范围内。代理会根据当前的水温获得奖励或惩罚。
# 然后，在最后的部分，代码运行了10个情节，每个情节中，代理都会随机选择行动，并且基于行动和环境的反馈更新得分。
# 1. Test Random Environment with OpenAI Gym
class ShowerEnv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up  # 定义可以采取的行动，down, stay, up
        self.action_space = Discrete(3)
        # Temperature array  # 定义观察空间，温度数组范围0-100
        self.observation_space = Box(low=np.array([0]), high=np.array([100]))
        # Set start temp  # 设置初始温度
        self.state = 38 + random.randint(-3, 3)
        # Set shower length  # 设置淋雨时间长度
        self.shower_length = 60

    def step(self, action):
        # Apply action
        # 0 -1 = -1 temperature
        # 1 -1 = 0
        # 2 -1 = 1 temperature
        self.state += action - 1
        # Reduce shower length by 1 second
        self.shower_length -= 1

        # Calculate reward
        if self.state >= 37 and self.state <= 39:
            reward = 1
        else:
            reward = -1

            # Check if shower is done
        if self.shower_length <= 0:
            done = True
        else:
            done = False

        # Apply temperature noise
        # self.state += random.randint(-1,1)
        # Set placeholder for info
        info = {}

        # Return step information
        return self.state, reward, done, info

    def render(self):
        # Implement viz
        pass

    def reset(self):
        # Reset shower temperature
        self.state = 38 + random.randint(-3, 3)
        # Reset shower time
        self.shower_length = 60
        return self.state


env = ShowerEnv()
print('env: ', env)

print('env.observation_space.sample(): ', env.observation_space.sample())

episodes = 10
for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        # env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(episode, score))

# 这段代码创建了一个深度学习模型，用于后续的强化学习任务。该模型由三层组成：两个使用ReLU激活函数的隐藏层和一个使用线性激活函数的输出层。
# 输入层根据环境的状态空间的形状来确定其结构，输出层的单元数量则由动作空间的大小决定。这样设计的模型可以根据给定的环境状态预测采取每个可能动作的预期回报。
# 2. 使用Keras创建一个深度学习模型
import numpy as np
# 从Keras库导入所需的模块
from tensorflow.keras.models import Sequential  # 用于初始化神经网络
from tensorflow.keras.layers import Dense, Flatten  # Dense用于添加全连接层，Flatten用于数据扁平化
from tensorflow.keras.optimizers import Adam  # 导入优化器Adam

# 获取环境的状态空间和动作空间的大小
states = env.observation_space.shape
actions = env.action_space.n

# 打印动作的数量
print(actions)

# 定义建立模型的函数
def build_model(states, actions):
    model = Sequential()  # 初始化模型
    # 添加输入层，隐藏层。使用relu激活函数，states作为输入形状
    model.add(Dense(24, activation='relu', input_shape=states))
    model.add(Dense(24, activation='relu'))  # 添加另一个隐藏层
    # 添加输出层，输出的单元数量等于可能的动作数量，使用线性激活函数
    model.add(Dense(actions, activation='linear'))
    return model  # 返回构建的模型

# del model  # 如果需要，可以删除之前构建的模型

# 调用函数，构建并存储模型
model = build_model(states, actions)
# 打印模型摘要，以查看模型的架构和参数
print(model.summary())


# 这段代码主要完成了代理的构建、训练、测试和权重的保存加载。首先，通过定义build_agent函数创建了一个DQN代理，该函数配置了代理的策略、记忆和其他参数。
# 然后编译并训练了代理。在训练完成后，代理被测试，以评估其性能。
# 其次，代理的权重被保存，然后删除了当前的模型、代理和环境，接着重新加载了模型和权重，并在新环境中测试了代理的性能。
# 3. 使用Keras-RL构建代理
from rl.agents import DQNAgent  # 导入DQNAgent用于创建代理
from rl.policy import BoltzmannQPolicy  # 导入策略
from rl.memory import SequentialMemory  # 导入记忆库


# 定义构建代理的函数
def build_agent(model, actions):
    policy = BoltzmannQPolicy()  # 使用Boltzmann策略
    memory = SequentialMemory(limit=50000, window_length=1)  # 定义记忆库大小和窗口长度
    # 创建DQN代理
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn  # 返回创建的代理

# 调用函数，创建并存储代理
dqn = build_agent(model, actions)
# 编译代理，使用Adam优化器和mean absolute error作为度量标准
dqn.compile(Adam(lr=1e-3), metrics=['mae'])
# 训练代理，在环境中执行50000步
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)

# 测试代理，在环境中执行100个情节，并打印平均奖励
scores = dqn.test(env, nb_episodes=100, visualize=False)
print(np.mean(scores.history['episode_reward']))

# 以可视化方式测试代理执行15个情节
_ = dqn.test(env, nb_episodes=15, visualize=True)

# 4. 从记忆中重新加载代理
# 保存代理的权重
dqn.save_weights('dqn_weights.h5f', overwrite=True)
# 删除模型，代理和环境
del model
del dqn
del env

# 创建新的环境，模型和代理
env = gym.make('CartPole-v0')
actions = env.action_space.n
states = env.observation_space.shape[0]
model = build_model(states, actions)
dqn = build_agent(model, actions)
# 编译代理
dqn.compile(Adam(lr=1e-3), metrics=['mae'])
# 加载之前保存的权重
dqn.load_weights('dqn_weights.h5f')
# 以可视化方式测试代理执行5个情节
_ = dqn.test(env, nb_episodes=5, visualize=True)







