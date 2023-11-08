from paddlenlp import Taskflow
docprompt = Taskflow("document_intelligence")
print(docprompt([{"doc": "./pic/resume.png", "prompt":["五百丁本次想要担任的是什么职位?", "五百丁是在哪里上的大学?", "大学学的是什么专业?", "年龄?", "民族"]}]))

