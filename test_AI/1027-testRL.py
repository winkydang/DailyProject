import gym  # 导入gym模块

# 创建并初始化CartPole-v1环境
env = gym.make('CartPole-v1')
env.reset()  # 重置环境，开始新的回合

# 运行1000个时间步
for _ in range(1000):
    env.render()  # 显示/渲染环境的当前状态

    # 从动作空间中随机选择一个动作
    action = env.action_space.sample()

    # 执行选择的动作，并获取环境返回的结果
    observation, reward, done, truncated, info = env.step(action)

    # 如果回合结束（done为True），则重置环境
    if done:
        env.reset()

    # 关闭环境，释放资源
env.close()
