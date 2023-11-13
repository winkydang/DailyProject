# 推理代码
#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author   :    Junhui Yu


import glob

import pandas as pd
import numpy as np
import re
import fitz

import lightgbm as lgb

patter = r"[\D]+(1\d{10})+(?!\d)"


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
        len(re.compile(patter).findall(text)),
        1 if '正样本' in path else 0,

    ]
    return feat


df = pd.DataFrame(
    columns=[
        'page_nums',
        'text_len',
        'text_len_mean',
        'text_len_max',
        'text_len_std',
        'text_set_len',
        'lentext-lenset',
        'lenset_div_lentext',
        'text_split_len',
        'text_split_ent_len',
        '-_nums',
        'x_nums',
        'xxx_nums',
        'dig_sum',
        '@_nums',
        '.com_nums',
        '*_nums',
        '：_nums',
        '****_nums',
        'phone_nums',
        'label'
    ])

test_paths = glob.glob('/work/data/integrity-check-of-resume-test-set/*.pdf')[:]

for t_f in test_paths:
    df.loc[len(df)] = extract_feature_from_pdf(t_f)

not_use_feats = ['label']
use_features = [col for col in df.columns if col not in not_use_feats]

model = lgb.Booster(model_file='model.txt')

y_pred = model.predict(df[use_features])

predict_label = np.argmax(y_pred, axis=1)

pd.DataFrame({
    'ResumeID': [x.split('/')[-1] for x in test_paths],
    'label': predict_label.astype(int)
}).to_csv('/work/output/result.csv', index=None)

