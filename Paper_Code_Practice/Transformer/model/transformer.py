import torch
from torch import nn

from model.encoder import Encoder
from model.decoder import Decoder

class Transformer(nn.Module):
    def __init__(self, n_input_vocab, n_output_vocab, d_model, head, d_ff, max_len, padding_idx, dropout, n_layers, device):
        super().__init__()
        self.padding_idx = padding_idx
        self.device = device

        # Encoder
        self.encoder = Encoder(n_input_vocab=n_input_vocab, 
                               d_model=d_model, 
                               head=head, 
                               d_ff=d_ff, 
                               max_len=max_len, 
                               padding_idx=padding_idx, 
                               dropout=dropout, 
                               n_layers=n_layers,
                               device=device)
        
        # Decoder
        self.decoder = Decoder(n_output_vocab=n_output_vocab, 
                               d_model=d_model, 
                               head=head, 
                               d_ff=d_ff, 
                               max_len=max_len, 
                               padding_idx=padding_idx, 
                               dropout=dropout, 
                               n_layers=n_layers,
                               device=device)
        
        # linear layer [batch_size, seq_len, n_output_vocab]
        self.linear = nn.Linear(d_model, n_output_vocab)

    def forward(self, src, tgt):
        # 1. 입력에 따른 mask 생성
        padding_mask = self.make_padding_mask(src, src)
        enc_dec_padding_mask = self.make_padding_mask(tgt, src)
        look_ahead_mask = self.make_padding_mask(tgt, tgt) * self.make_look_ahead_mask(tgt)

        # 2. encoder
        memory = self.encoder(src, padding_mask)

        # 3. decoder
        output = self.decoder(tgt, memory, look_ahead_mask, enc_dec_padding_mask)

        # 4. linear layer
        output = self.linear(output)
        
        return output

    def make_padding_mask(self, q, k):
        # q,k의 size = [batch_size, seq_len]
        _, q_seq_len = q.size()
        _, k_seq_len = k.size()

        q = q.ne(self.padding_idx)  # padding token을 0, 나머지를 1로 만들어줌
        q = q.unsqueeze(1).unsqueeze(3) # [batch_size, 1, q_seq_len, 1]
        q = q.repeat(1,1,1,k_seq_len)   # [batch_size, 1, q_seq_len, k_seq_len]

        k = k.ne(self.padding_idx)
        k = k.unsqueeze(1).unsqueeze(2) # [batch_size, 1, 1, k_seq_len]
        k = k.repeat(1,1,q_seq_len,1)   # [batch_size, 1, q_seq_len, k_seq_len]

        # and 연산
        # [batch_size, 1, q_seq_len, k_seq_len]
        mask = q & k

        return mask
    
    def make_look_ahead_mask(self, tgt):
        _, seq_len = tgt.size()

        # torch.tril 함수를 사용하여 한칸씩 밀려나며 마스킹을 해줌
        # [seq_len,seq_len]
        mask = torch.tril(torch.ones(seq_len,seq_len)).type(torch.BoolTensor).to(self.device)

        return mask