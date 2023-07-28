"""
本例子中使用 openAI ChatGPT 作为决策模型，利用两个【工具】：搜索、计算解决问题。
"""
import os

import openai

# 设置代理服务器的配置。 通过'proxies'字典设置代理服务器的地址和端口。
proxies = {'http': "http://127.0.0.1:7890",
           'https': "http://127.0.0.1:7890"}
openai.proxy = proxies

# 设置 OpenAI API 密钥
os.environ["OPENAI_API_KEY"] = "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"

# 设置SerpApi API 密钥
os.environ["SERPAPI_API_KEY"] = "be810684e6058f5286be699986dd25bad5bda01e17aa9675f3e37674dd15a71c"

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain import OpenAI

# 创建 OpenAI 语言模型对象，设置温度为 0. 这个对象将用于处理语言生成任务。
llm = OpenAI(temperature=0)

# 加载所需的工具（例如 serpapi 和 llm-math）
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# 初始化代理（根据需要使用的代理类型）
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行代理，传入需要处理的问题
# agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")
agent.run("What is the capital of American? What is the temperature of that city? Please express it in degrees Celsius.")
