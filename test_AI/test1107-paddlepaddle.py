# 参考链接：https://mp.weixin.qq.com/s/3l4NvGfy8LaKuj_3HGH5pg   文档智能：ERNIE-Layout
# https://github.com/PaddlePaddle/PaddleNLP/tree/develop/model_zoo/ernie-layout

from paddlenlp import Taskflow
docprompt = Taskflow("document_intelligence")
# print(docprompt([{"doc": "./pic/resume.png", "prompt":["五百丁本次想要担任的是什么职位?", "五百丁是在哪里上的大学?", "大学学的是什么专业?", "年龄?", "民族"]}]))
# print(docprompt([{"doc": "./pic/resume-1.png", "prompt":["王尊本次想要担任的是什么职位?", "五百丁是在哪里上的大学?", "大学学的是什么专业?", "年龄?", "电话"]}]))
print(docprompt([{"doc": "./pic/resume-2.png", "prompt":["本次想要担任的是什么职位?", "是在哪里上的大学?", "大学学的是什么专业?", "年龄?", "电话"]}]))

