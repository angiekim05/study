import re
from konlpy.tag import Komoran
import spacy

from torch.utils.data import Dataset

import torch
from torch.nn.utils.rnn import pad_sequence

import random

tokenizer = Komoran()
spacy_en = spacy.load('en_core_web_sm')

# tokenizer
def tokenizer_ko(text):
    return tokenizer.morphs(text)
def tokenizer_en(text):
    return [token.text for token in spacy_en.tokenizer(text)]

# normalize
def normalizeString(s):
    s = s.lower().strip()
    s = re.sub(r'[^a-zA-Z0-9가-힣.!?]+' ,r' ',s)
    return s

# tokenize sentences in file
def tokenize_ko_dataset(data_path):
    with open(data_path) as f:
        dataset = []
        idxs = []
        for idx,x in enumerate(f.readlines()):
            x = normalizeString(x).strip()
            if re.sub(r'[^a-z]',r"",x): # 영어가 있다면 넘어감 (일부 데이터의 ko-en set이 일치하지 않기 때문)
                continue
            if len(x) > 2:
                dataset.append(tokenizer_ko(x))
                idxs.append(idx)
    return idxs, dataset

def tokenize_en_dataset(data_path, idxs, src):
    with open(data_path) as f:
        dataset = []
        datas = f.readlines()
        d = 0
        for i in range(len(idxs)):
            x = tokenizer_en(normalizeString(datas[idxs[i]]).strip())
            if len(x) < 2:  # 한글은 긴 문장인데 반해 단어가 없는 영문장이 있음으로 제외
                del src[i-d]
                d += 1
            else:
                dataset.append(x)
    return src, dataset

# tokenize single sentence
def tokenize_ko_sen(s):
    data = tokenizer_ko(normalizeString(s).strip())
    return data

def tokenize_en_sen(s):
    data = tokenizer_en(normalizeString(s).strip())
    return data

# special token
unk_token_idx = 0
pad_token_idx = 1
sos_token_idx = 2
eos_token_idx = 3

# encode
def encode(data,stoi):
    encoded = []
    for x in data:
        encoded.append(
            [sos_token_idx]
            + [stoi.get(token,unk_token_idx) for token in x]
            + [eos_token_idx]
        )
    return encoded

# decode
# itos 사전을 통해 숫자 -> 단어
def decode(data,itos):
    output = []
    for sentence in data:
        s = []
        for idx in sentence:
            word = itos[int(idx)]
            if word[0] == "<":
                # eos 토큰이 나오면 이후는 모두 pad 토큰임으로 멈춤
                if idx == eos_token_idx:
                    break
                continue # sos 토큰일 경우 건너뜀
            s.append(word)
        output.append(s)
    return output

# custom Dataset
class CustomDataset(Dataset):
    def __init__(self, src, tgt):
        self.dataset = [(src[i], tgt[i]) for i in range(len(src))]

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        return self.dataset[idx]

# batch sampler
class BucketingSampler():
    def __init__(self, ko_cnt, en_cnt, batch_size=1,random_seed=False):
        data_len = [(x, y, idx) for idx,(x, y) in enumerate(zip(ko_cnt,en_cnt))]
        data_len.sort()
        data_idx = [data[2] for data in data_len]
        self.bins = [data_idx[i:i+batch_size] for i in range(0,len(data_idx), batch_size)]
        
        # seed 설정
        if random_seed:
            random.seed(random_seed)
            
        # 모델이 batch 길이에 편향되지 않도록 섞음
        random.shuffle(self.bins) 
    
    def __len__(self):
        return len(self.bins)

    def __iter__(self):
        for idx_set in self.bins:
            yield idx_set

# batch length에 맞춰 padding token 채워줌
def collate_fn(batch_samples):
    pad_token_idx = 1
    src_sentences = pad_sequence([torch.tensor(src) for src, _ in batch_samples], batch_first=True, padding_value=pad_token_idx)
    tgt_sentences = pad_sequence([torch.tensor(tgt) for _, tgt in batch_samples], batch_first=True, padding_value=pad_token_idx)
    return src_sentences, tgt_sentences