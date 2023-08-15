# import argparse
# from transformers import AutoTokenizer
# tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
# from model import chat, VisualGLMModel
# model, model_args = VisualGLMModel.from_pretrained('visualglm-6b',
# args=argparse.Namespace(fp16=True, skip_init=True))
# from sat.model.mixins import CachedAutoregressiveMixin
# model.add_mixin('auto-regressive', CachedAutoregressiveMixin())
# image_path = "your image path or URL"
# response, history, cache_image = chat(image_path, model, tokenizer, "描述这张图片。", history=[])
# print(response)
# response, history, cache_image = chat(None, model, tokenizer, "这张图片可能是在什么场所拍摄的？", history=history, image=cache_image)
# print(response)

import torch
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(device)  # mps
print(torch.backends.mps.is_available())  # True
print(torch.backends.mps.is_built())  # True
