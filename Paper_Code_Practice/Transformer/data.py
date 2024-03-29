import os
from config import *

from torchtext.vocab import build_vocab_from_iterator
from torch.utils.data import DataLoader

import time
start_time = time.time()
print("Data preprocessing...")
from util.data_util import *

if not os.path.exists(f'{save_path}dataset'):
    os.makedirs(f'{save_path}dataset')
if not os.listdir(f'{save_path}dataset'):
    from dataset.dataset_setup import *
    print("Data Tokenizing...")
    # train,test,valid = 76125,1603,792
    train_idx, train_src = tokenize_ko_dataset("dataset/dataset/korean-english-park.train.ko") # max token length = 129
    valid_idx, valid_src = tokenize_ko_dataset("dataset/dataset/korean-english-park.dev.ko") # max token length = 90
    test_idx, test_src = tokenize_ko_dataset("dataset/dataset/korean-english-park.test.ko") # max token length = 107
    train_src, train_tgt = tokenize_en_dataset("dataset/dataset/korean-english-park.train.en", train_idx, train_src) # max token length = 96
    valid_src, valid_tgt = tokenize_en_dataset("dataset/dataset/korean-english-park.dev.en", valid_idx, valid_src) # max token length = 71
    test_src, test_tgt = tokenize_en_dataset("dataset/dataset/korean-english-park.test.en", test_idx, test_src) # max token length = 74

    # data save
    with open(f"{save_path}dataset/train_src.txt", "w") as f:
        for data in train_src:
            f.write("_".join(data)+"\n")
    with open(f"{save_path}dataset/valid_src.txt", "w") as f:
        for data in valid_src:
            f.write("_".join(data)+"\n")
    with open(f"{save_path}dataset/test_src.txt", "w") as f:
        for data in test_src:
            f.write("_".join(data)+"\n")
    with open(f"{save_path}dataset/train_tgt.txt", "w") as f:
        for data in train_tgt:
            f.write("_".join(data)+"\n")
    with open(f"{save_path}dataset/valid_tgt.txt", "w") as f:
        for data in valid_tgt:
            f.write("_".join(data)+"\n")
    with open(f"{save_path}dataset/test_tgt.txt", "w") as f:
        for data in test_tgt:
            f.write("_".join(data)+"\n")
    print("Tokenization complete")

else:
    train_src = []
    with open(f"{save_path}dataset/train_src.txt", "r") as f:
        for data in f.readlines():
            train_src.append(data.strip().split("_"))
    valid_src = []
    with open(f"{save_path}dataset/valid_src.txt", "r") as f:
        for data in f.readlines():
            valid_src.append(data.strip().split("_"))
    test_src = []
    with open(f"{save_path}dataset/test_src.txt", "r") as f:
        for data in f.readlines():
            test_src.append(data.strip().split("_"))
    train_tgt = []
    with open(f"{save_path}dataset/train_tgt.txt", "r") as f:
        for data in f.readlines():
            train_tgt.append(data.strip().split("_"))
    valid_tgt = []
    with open(f"{save_path}dataset/valid_tgt.txt", "r") as f:
        for data in f.readlines():
            valid_tgt.append(data.strip().split("_"))
    test_tgt = []
    with open(f"{save_path}dataset/test_tgt.txt", "r") as f:
        for data in f.readlines():
            test_tgt.append(data.strip().split("_"))

# ko vocab: 35857 
# en vocab: 42217
vocab_ko = build_vocab_from_iterator(train_src, min_freq=2, specials=["<unk>", "<pad>", "<sos>", "<eos>"])
vocab_en = build_vocab_from_iterator(train_tgt, min_freq=2, specials=["<unk>", "<pad>", "<sos>", "<eos>"])

ko_stoi = vocab_ko.vocab.get_stoi()
en_stoi = vocab_en.vocab.get_stoi()
ko_itos = vocab_ko.vocab.get_itos()
en_itos = vocab_en.vocab.get_itos()

train_src = encode(train_src,ko_stoi)
valid_src = encode(valid_src,ko_stoi)
test_src = encode(test_src,ko_stoi)
train_tgt = encode(train_tgt,en_stoi)
valid_tgt = encode(valid_tgt,en_stoi)
test_tgt = encode(test_tgt,en_stoi)

# batch sampler
train_sampler = BucketingSampler(train_src,train_tgt, 
                           batch_size = batch_size)
valid_sampler = BucketingSampler(valid_src,valid_tgt, 
                           batch_size = batch_size)
test_sampler = BucketingSampler(test_src,test_tgt, 
                           batch_size = batch_size)

# dataset
train_dataset = CustomDataset(train_src,train_tgt)
valid_dataset = CustomDataset(valid_src,valid_tgt)
test_dataset = CustomDataset(test_src,test_tgt)

# dataloader
train_loader = DataLoader(dataset=train_dataset,
                          batch_sampler=train_sampler,
                          collate_fn=collate_fn)
valid_loader = DataLoader(dataset=valid_dataset,
                          batch_sampler=valid_sampler,
                          collate_fn=collate_fn)
test_loader = DataLoader(dataset=test_dataset,
                         batch_sampler=test_sampler,
                         collate_fn=collate_fn)

end_time = time.time()
mins, secs = divmod(end_time-start_time,60)
print(f"All data is ready. Time: {int(mins)}m {secs:.2f}s")