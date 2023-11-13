# 本次比赛主要使用的是lightgbm的树模型，视为二分类任务，进行10折交叉验证的训练。
#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author   :    Junhui Yu

import warnings

warnings.simplefilter('ignore')

import gc

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, classification_report

import lightgbm as lgb

import glob

import pandas as pd
from tqdm import tqdm
import numpy as np
import re
import fitz

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


train_paths = glob.glob(
    '../xfdata/校招简历信息完整性检测训练集/*/*.pdf')

df_train = pd.DataFrame(
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

for t_p in tqdm(train_paths):
    df_train.loc[len(df_train)] = extract_feature_from_pdf(t_p)

not_use_feats = ['label']
use_features = [col for col in df_train.columns if col not in not_use_feats]
print(len(use_features))
train = df_train[df_train['label'].notna()]

NUM_CLASSES = 2
FOLDS = 10
TARGET = 'label'


def run_lgb(df_train, use_features):
    target = TARGET
    oof_pred = np.zeros((len(df_train), NUM_CLASSES))

    folds = StratifiedKFold(n_splits=FOLDS, shuffle=True, random_state=42)
    for fold, (tr_ind, val_ind) in enumerate(folds.split(train, train[TARGET])):
        print(f'Fold {fold + 1}')
        x_train, x_val = df_train[use_features].iloc[tr_ind], df_train[use_features].iloc[val_ind]
        y_train, y_val = df_train[target].iloc[tr_ind], df_train[target].iloc[val_ind]
        train_set = lgb.Dataset(x_train, y_train)
        val_set = lgb.Dataset(x_val, y_val)

        params = {
            'learning_rate': 0.1,
            'metric': 'multiclass',
            'objective': 'multiclass',
            'num_classes': NUM_CLASSES,
            'feature_fraction': 0.75,
            'bagging_fraction': 0.75,
            'bagging_freq': 2,
            'n_jobs': -1,
            'seed': 1029,
            'max_depth': 10,
            'num_leaves': 100,
            'lambda_l1': 0.5,
            'lambda_l2': 0.8,
            'verbose': -1
        }

        model = lgb.train(params,
                          train_set,
                          num_boost_round=500,
                          early_stopping_rounds=100,
                          valid_sets=[train_set, val_set],
                          verbose_eval=100)
        oof_pred[val_ind] = model.predict(x_val)
        print('acc:', accuracy_score(np.argmax(oof_pred, axis=1), df_train['label']))
        del x_train, x_val, y_train, y_val, train_set, val_set
        gc.collect()

    return oof_pred, model


oof_pred, model = run_lgb(train, use_features)
print(classification_report(np.argmax(oof_pred, axis=1), df_train['label']))

model.save_model('model.txt')