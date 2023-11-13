# # 导入gradio
# import gradio as gr
# # 导入transformers相关包
# from transformers import *
# # 通过Interface加载pipeline并启动文本分类服务
# gr.Interface.from_pipeline(pipeline("text-classification", model="uer/roberta-base-finetuned-dianping-chinese")).launch()


# 阅读理解
# 导入gradio
import gradio as gr
# ＃导入transformers相关包
from transformers import *
# ＃ 通过Interface加载pipeline并启动阅读理解服务
gr.Interface.from_pipeline(pipeline("question-answering", model="uer/roberta-base-chinese-extractive-qa")).launch()

