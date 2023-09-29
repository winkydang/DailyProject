# Fine-Tune Your Own Llama 2 Model in a Colab Notebook    https://colab.research.google.com/drive/1PEQyJO1-f6j0S_XJ8DV50NkpzasXkrzd?usp=sharing#scrollTo=OSHlAbqzDFDq
# https://towardsdatascience.com/fine-tune-your-own-llama-2-model-in-a-colab-notebook-df9823a04a32
# 导入os模块，该模块提供了一种使用操作系统相关功能的方法，例如读取或写入文件。
import os

# 导入PyTorch库，这是一个用于深度学习的开源库。
import torch

# 从datasets库中导入load_dataset函数，该库是huggingface公司的项目，主要用于加载和处理数据集。
from datasets import load_dataset

# 从transformers库中导入了多个模块和函数：
# AutoModelForCausalLM: 自动加载适合因果语言建模的预训练模型。
# AutoTokenizer: 自动化地加载预训练模型的相关分词器。
# BitsAndBytesConfig: 配置类，可能与模型的某些配置有关。
# HfArgumentParser: HuggingFace提供的参数解析工具，用于简化脚本参数的处理。
# TrainingArguments: 包含与训练相关的所有参数的类。
# pipeline: 用于创建模型处理流水线的工具。
# logging: 用于记录日志。
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)

# 从peft库中导入LoraConfig和PeftModel，不过我不熟悉这个库和它提供的功能。可能是某个具体的项目或者库。
from peft import LoraConfig, PeftModel

# 从trl库中导入SFTTrainer，也不是一个我熟悉的库。可能是用于特定的训练任务。
from trl import SFTTrainer

# 定义想要从Hugging Face hub训练的模型名称
model_name = "NousResearch/Llama-2-7b-chat-hf"

# 定义要使用的指令数据集的名称
dataset_name = "mlabonne/guanaco-llama2-1k"

# 给微调后的模型定义一个名称
new_model = "llama-2-7b-miniguanaco"

# LoRA的注意力维度。
lora_r = 64

# LoRA缩放的Alpha参数。
lora_alpha = 16

# LoRA层的dropout概率。
lora_dropout = 0.1

# 激活4位精度的基模型加载。
use_4bit = True

# 4位基模型的计算dtype。
bnb_4bit_compute_dtype = "float16"

# 量化类型 (fp4 or nf4)。
bnb_4bit_quant_type = "nf4"

# 为4位基模型激活嵌套量化(双重量化)。
use_nested_quant = False

################################################################################
# TrainingArguments parameters
################################################################################

# 定义保存模型预测和检查点的输出目录
output_dir = "./results"
# 训练周期的数量
num_train_epochs = 1
# 启用fp16/bf16训练
fp16 = False
bf16 = False
# 定义每个GPU的训练批次大小
per_device_train_batch_size = 4
# 定义每个GPU的评估批次大小
per_device_eval_batch_size = 4
# 定义要累积梯度的更新步骤数量
gradient_accumulation_steps = 1
# 启用梯度检查点
gradient_checkpointing = True
# 最大梯度正态（梯度裁剪）
max_grad_norm = 0.3
# 初始学习率（AdamW优化器）
learning_rate = 2e-4
# 应用于除偏置/LayerNorm权重之外的所有层的权重衰减
weight_decay = 0.001
# 要使用的优化器
optim = "paged_adamw_32bit"
# 学习率调度
lr_scheduler_type = "cosine"
# 训练步骤的数量（覆盖num_train_epochs）
max_steps = -1
# 从0到学习率的线性预热的步骤比率
warmup_ratio = 0.03
# 将具有相同长度的序列分组到批次中
group_by_length = True
# 每X更新步骤保存一次检查点
save_steps = 0
# 每X更新步骤记录一次日志
logging_steps = 25

################################################################################
# SFT parameters
################################################################################

# 定义要使用的最大序列长度
max_seq_length = None
# 在同一输入序列中打包多个短示例以提高效率
packing = False
# 在GPU 0上加载整个模型
device_map = {"": 0}















