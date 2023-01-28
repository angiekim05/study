import torch
from torch import nn

from nltk.translate.bleu_score import corpus_bleu

from data import *
from model.transformer import Transformer

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
if model_version == "":
    try:
        latest_version = sorted(os.listdir(f'{save_path}saved'))[0]
        model.load_state_dict(torch.load(f'{save_path}saved/{latest_version}'))
    except Exception as e:
        raise SystemExit(e)
else:
    try:
        model.load_state_dict(torch.load(f'{save_path}saved/model-{model_version}.pt'))
    except Exception as e:
        raise SystemExit(e)

criterion = nn.CrossEntropyLoss(ignore_index=padding_idx)

def test(model, data_source, criterion):
    model.eval() # evaluation mode (deactivate dropout)
    epoch_loss = 0
    epoch_bleu = 0
    epoch_bleu_1 = 0
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
            bleu_1 = corpus_bleu(list_of_references=tgt_words, 
                              hypotheses=output_words,
                              weights=(1,0,0,0))
            epoch_bleu += bleu
            epoch_bleu_1 += bleu_1
    
    print(f"Test Loss: {epoch_loss / n_batch:.5f}| BLEU Score: {epoch_bleu / n_batch * 100:.3f} | BLEU 1_gram Score: {epoch_bleu_1 / n_batch * 100:2.3f} ") 

if __name__ == '__main__':
    test(model, test_loader, criterion)