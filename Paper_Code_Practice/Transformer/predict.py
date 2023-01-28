import argparse
import torch

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

s = "안녕하세요 만나서 반가워요"
def get_src(s):
    src = encode([tokenize_ko_sen(s)],ko_stoi)
    return torch.tensor(src)
def get_init_tgt():
    tgt = [[sos_token_idx]]
    return torch.tensor(tgt)

def predict(model):
    # input 받기
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", 
        default="안녕", 
        type=str, 
        help="Korean setence that you want to translate"
    )
    args = parser.parse_args()
    input = args.input

    src = get_src(input).to(device)
    tgt = get_init_tgt.to(device)

    model.eval() # evaluation mode (deactivate dropout)
    with torch.no_grad():
        for _ in range(max_len):
            output = model(src,tgt)
            last_word = output[:,-1:,:].max(dim=-1)[1]

            # eos token을 만나면 끝냄
            if torch.equal(last_word, torch.tensor([[eos_token_idx]])):
                break

            # next tgt
            tgt = torch.cat([tgt,last_word],dim=-1)

        # decode tgt
        tgt_words = decode(tgt,en_itos)

    return "".join(tgt_words)

if __name__ == '__main__':
    predict(model)