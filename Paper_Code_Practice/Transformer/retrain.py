import torch
from torch import nn, optim

import time
from nltk.translate.bleu_score import corpus_bleu

from data import *
from model.transformer import Transformer
from util.scheduler import LRScheduler

from tqdm import tqdm

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
# model load
if retrain_version == "":
    try:
        latest_version = sorted(os.listdir(f'{save_path}saved'))[0]
        model.load_state_dict(torch.load(f'{save_path}saved/{latest_version}'))
    except:
        raise SystemExit('There is no saved model')
else:
    try:
        model.load_state_dict(torch.load(f'{save_path}saved/model-{retrain_version}.pt'))
    except:
        raise SystemExit('Can not find version')


optimizer = optim.Adam(params=model.parameters(),
                       lr=init_lr,
                       betas=(beta1, beta2), 
                       eps=eps,
                       weight_decay=weight_decay)

scheduler = LRScheduler(optimizer, d_model=d_model, warmup_steps=warmup_steps)

# 기본적으로 많이 사용되는 스케줄러
# scheduler = optim.lr_scheduler.StepLR(optimizer, 1.0, gamma=0.95)

criterion = nn.CrossEntropyLoss(ignore_index=padding_idx)

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

print(f'The model has {count_parameters(model)} trainable parameters')

def train(model, data_source, optimizer, criterion, idx):
    model.train() # train mode
    epoch_loss = 0
    n_batch = len(data_source)
    with tqdm(data_source, unit="batch") as tepoch:
        tepoch.set_description(f"Train Epoch {idx}")
        for i, batch in enumerate(tepoch):
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

            if i % log_interval == 0 and i > 0: # 0 이상의 interval 간격마다 loss 값 찍기
                print(f'| train_loss : {loss.item():5.5f} |')
        
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
    train_losses, valid_losses, bleus = [], [], []
    if not os.path.exists(f"{save_path}saved"):
        os.makedirs(f"{save_path}saved")
    if not os.path.exists(f"{save_path}result"):
        os.makedirs(f"{save_path}result")
    total_start_time = time.time()
    for step in range(epoch):
        start_time = time.time()
        train_loss = train(model, train_loader, optimizer, criterion, step+1)
        valid_loss, bleu = evaluate(model, valid_loader, criterion)
        end_time = time.time()

        scheduler.step()

        train_losses.append(train_loss)
        valid_losses.append(valid_loss)
        bleus.append(bleu)

        epoch_mins, epoch_secs = divmod(end_time-start_time,60)
        total_mins, total_secs = divmod(end_time-total_start_time,60)

        if valid_loss < best_loss:
            best_loss = valid_loss
            torch.save(model.state_dict(), f'{save_path}saved/model-{valid_loss}.pt')
            
        f = open(f'{save_path}result/train_loss.txt', 'w')
        f.write(str(train_losses))
        f.close()

        f = open(f'{save_path}result/bleu.txt', 'w')
        f.write(str(bleus))
        f.close()

        f = open(f'{save_path}result/valid_loss.txt', 'w')
        f.write(str(valid_losses))
        f.close()

        print(f'Epoch: {step + 1} | Time: {int(total_mins)}m {total_secs:.2f}s | Epoch_Time: {int(epoch_mins)}m {epoch_secs:.2f}s | Train Loss: {train_loss:.5f} | Val Loss: {valid_loss:.5f} | BLEU Score: {bleu:.3f}')
    end_time = time.time()
    epoch_mins, epoch_secs = divmod(end_time-total_start_time,60)
    print(f'Time: {int(epoch_mins)}m {epoch_secs:.2f}s')

if __name__ == '__main__':
    run(epoch,inf)