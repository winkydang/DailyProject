from typing import re

import numpy as np
from fitz import fitz

pattern = r"[\D]+(1\d{10})+(?!\d)"

def extract_feature_from_pdf(path):
    doc = fitz.open(path)
    all_content = []
    page_nums = 0
    for i in doc.pages():
        page_nums += 1
        all_content.append(i.get_text())
    text = ''.join(all_content)
    text = ''.join(text.split('\n'))

    feat = [
        page_nums,
        len(text),
        np.mean([len(x) for x in text.split('\n')]),
        np.max([len(x) for x in text.split('\n')]),
        np.std([len(x) for x in text.split('\n')]),

        len(set(text)),
        len(text) - len(set(text)),
        len(set(text)) / (len(text) + 1),

        len(text.split()),
        len(text.split('\n')),
        text.count('-'),
        text.count('x'),
        text.count('xxx'),
        sum([text.count(x) for x in '0123456789']),
        text.count('@'),
        text.count('.com'),
        text.count('*'),
        text.count('：'),
        text.count('****'),
        len(re.compile(pattern).findall(text)),
        1 if '正样本' in path else 0,

    ]
    return feat
