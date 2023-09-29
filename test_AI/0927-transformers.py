from transformers import pipeline
# # 使用情绪分析流水线
# classifier = pipeline('sentiment-analysis')
# res = classifier('We are very happy to introduce pipeline to the transformers repository.')  # [{'label': 'POSITIVE', 'score': 0.9996980428695679}]
# # res = classifier('they just like rubbish.')  # [{'label': 'NEGATIVE', 'score': 0.999705970287323}]
# print(res)

# # 使用问答流水线
# question_answerer = pipeline('question-answering')
# # question_answerer({
# #      'question': 'What is the name of the repository ?',
# #      'context': 'Pipeline has been included in the huggingface/transformers repository'
# #  })  # {'score': 0.30970096588134766, 'start': 34, 'end': 58, 'answer': 'huggingface/transformers'}
# # res = question_answerer({
# #      'question': 'What is the name of the person?',
# #      'context': 'My name is winky, i come from China.'
# #  })
# # print(res)
# res = question_answerer({
#      'question': 'What is the gender of the person?',
#      'context': 'My name is winky, i come from China.'
#  })
# print(res)  # {'score': 0.9488672018051147, 'start': 11, 'end': 16, 'answer': 'winky'}
#
# res2 = question_answerer({
#      'question': 'What is the gender of winky?',
#      'context': 'My name is winky, i come from China.'
#  })
# print(res2)  # {'score': 0.6194560527801514, 'start': 30, 'end': 35, 'answer': 'China'}
#
# res3 = question_answerer({
#      'question': 'What is the name of the person?',
#      'context': 'My name is winky, i come from China.'
#  })
# print(res3)  # {'score': 0.9948489665985107, 'start': 11, 'end': 16, 'answer': 'winky'}

# 要在你的任务上下载和使用任意预训练模型也很简单，只需三行代码。这里是 PyTorch 版的示例：
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

inputs = tokenizer("Hello world!", return_tensors="pt")
outputs = model(**inputs)
print(outputs)




