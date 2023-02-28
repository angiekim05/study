import argparse

import torch
from torch import nn, optim

import time
from nltk.translate.bleu_score import corpus_bleu

from data import *
from model.transformer import Transformer
from util.scheduler import LRScheduler

from tqdm import tqdm

def records(path,epoch=None):
    with open(path, 'r') as f:
        results = f.readline().split(", ")
        results[0] = results[0][1:]
        results[-1] = results[-1][:-1]
        results = list(map(float,results[:epoch]))
    return results
        
def record_v(save_path):
    valid_list = records(f'{save_path}result/valid_loss.txt')
    if overwrite:
        with open(f'{save_path}saved/saved_info.txt') as f:
            results = f.readline().split('|')
            last_epoch = int(results[0].split()[-1])
            valid_list = valid_list[:last_epoch]
            last_loss = valid_list[-1]
    elif model_version == "":
        last_loss, last_epoch = valid_list[-1], len(valid_list)
    else:
        last_loss = float(model_version)
        last_epoch = valid_list.index(last_loss)+1
    return valid_list, last_loss, last_epoch

if not os.path.exists(f"{save_path}saved"):
    raise SystemExit(f"No such directory: {save_path}saved")
if not os.path.exists(f"{save_path}result"):
    raise SystemExit(f"No such directory: {save_path}result")

valid_loss_list, last_loss, last_epoch = record_v(save_path)
train_loss_list = records(f'{save_path}result/train_loss.txt',last_epoch)
bleu_list = records(f'{save_path}result/bleu.txt',last_epoch)

n_input_vocab = len(vocab_ko)
n_output_vocab = len(vocab_en)

model = Transformer(n_input_vocab=n_input_vocab, 
                    n_output_vocab=n_output_vocab, 
                    n_layers=n_layers, 
                    d_model=d_model, 
                    d_ff=d_ff,
                    head=head,
                    dropout=dropout, 
                    max_len=max_len, 
                    padding_idx=padding_idx, 
                    device=device).to(device)

optimizer = optim.Adam(params=model.parameters(),
                       lr=init_lr,
                       betas=(beta1, beta2), 
                       eps=eps,
                       weight_decay=weight_decay)

scheduler = LRScheduler(optimizer, d_model=d_model, warmup_steps=warmup_steps)
scheduler.last_epoch = last_epoch

criterion = nn.CrossEntropyLoss(ignore_index=padding_idx)

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f'The model has {count_parameters(model)} trainable parameters')

def train(model, data_source, optimizer, criterion, idx):
    model.train() # train mode
    epoch_loss = 0
    n_batch = len(data_source)
    with tqdm(data_source, unit="batch", desc = f"Epoch {idx}") as tepoch:
        for batch in tepoch:
            src = batch[0].to(device)
            tgt = batch[1].to(device)

            optimizer.zero_grad()
            output = model(src,tgt[:,:-1])
            output_reshape = output.contiguous().view(-1,output.size(-1)) # (-1,vocab_size)
            tgt = tgt[:,1:].contiguous().view(-1)

            loss = criterion(output_reshape,tgt)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), clip) # parameter exploding 방지
            optimizer.step()

            epoch_loss += loss.item()

            # tqdm 으로 minibatch의 train loss 값 찍기
            tepoch.set_postfix({'minibatch_loss' : f'{loss.item():5.5f}'})
        
    return epoch_loss / n_batch

def evaluate(model, data_source, criterion):
    model.eval() # evaluation mode
    epoch_loss = 0
    epoch_bleu = 0
    n_batch = len(data_source)
    with torch.no_grad():
        for batch in data_source:
            src = batch[0].to(device)
            tgt = batch[1].to(device)

            output = model(src,tgt[:,:-1])
            output_reshape = output.contiguous().view(-1,output.size(-1)) # (-1,vocab_size)
            tgt_reshape = tgt[:,1:].contiguous().view(-1)

            loss = criterion(output_reshape,tgt_reshape)
            epoch_loss += loss.item()

            output_words = output.max(dim=-1)[1] # vocab 중 max 값의 index 가져오기
            output_words = decode(output_words,en_itos)
            tgt_words = decode(tgt,en_itos)
            bleu = corpus_bleu(list_of_references=tgt_words, 
                              hypotheses=output_words)
            epoch_bleu += bleu

    return epoch_loss / n_batch, epoch_bleu / n_batch

def run(epoch, best_loss):
    total_start_time = time.time()
    for step in range(last_epoch, epoch):
        start_time = time.time()
        train_loss = train(model, train_loader, optimizer, criterion, step+1)
        valid_loss, bleu = evaluate(model, valid_loader, criterion)
        end_time = time.time()

        scheduler.step()

        epoch_mins, epoch_secs = divmod(end_time-start_time,60)
        total_mins, total_secs = divmod(end_time-total_start_time,60)
        total_hours, total_mins = divmod(total_mins,60)

        valid_loss = round(valid_loss,10)
        train_loss_list.append(train_loss)
        valid_loss_list.append(valid_loss)
        bleu_list.append(bleu)

        with open(f'{save_path}result/train_loss.txt', 'w') as f:  
            f.write(str(train_loss_list))

        with open(f'{save_path}result/bleu.txt', 'w') as f:
            f.write(str(bleu_list))

        with open(f'{save_path}result/valid_loss.txt', 'w') as f:
            f.write(str(valid_loss_list))

        if valid_loss < best_loss:
            best_loss = valid_loss
            if overwrite:
                torch.save(model.state_dict(), f'{save_path}saved/model.pt')
                with open(f'{save_path}saved/saved_info.txt', 'w') as f:
                    f.write(f"Epoch {step + 1:4} | Val Loss: {valid_loss:.5f} | Train Loss: {train_loss:.5f} | BLEU Score: {bleu*100:2.3f}")
            else:
                torch.save(model.state_dict(), f'{save_path}saved/model_{valid_loss}.pt')

        print(f'Epoch {step + 1:4} | Time: {int(total_hours):3}h {int(total_mins):02}m {total_secs:02.2f}s | Epoch_Time: {int(epoch_mins)}m {epoch_secs:.2f}s | Train Loss: {train_loss:.5f} | Val Loss: {valid_loss:.5f} | BLEU Score: {bleu*100:2.3f}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model", 
        default="", 
        type=str, 
        help="Model version: default means the latest version (the smallest valid loss version)"
    )
    args = parser.parse_args()
    model_version = args.model

    # model load
    if model_version == "":
        try:
            latest_version = sorted(os.listdir(f'{save_path}saved'))
            for version in latest_version:
                if version[-3:] == ".pt":
                    latest_version = version
                    break
            model.load_state_dict(torch.load(f'{save_path}saved/{latest_version}'))
        except Exception as e:
            raise SystemExit(e)
    else:
        try:
            model.load_state_dict(torch.load(f'{save_path}saved/model_{model_version}.pt'))
        except Exception as e:
            raise SystemExit(e)

    run(epoch,last_loss)