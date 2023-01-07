from torch import nn

from model.layers.embedding.positional_encoding import PositionalEncoding
from model.layers.encoder_layer import EncoderLayer

class Encoder(nn.Module):
    def __init__(self, n_input_vocab, d_model, head, d_ff, max_len, padding_idx, dropout, n_layers, device):
        super().__init__()

        # input embbeding
        self.input_emb = nn.Embedding(n_input_vocab, d_model, padding_idx=padding_idx)
        self.pos_encoding = PositionalEncoding(d_model, max_len, device)
        self.dropout = nn.Dropout(p=dropout)

        # n 개의 encoder layer
        self.encoder_layers = nn.ModuleList([EncoderLayer(d_model=d_model, 
                                                         head=head, 
                                                         d_ff=d_ff, 
                                                         dropout=dropout)
                                             for _ in range(n_layers)])

    def forward(self, x, padding_mask):
        # 1. input embedding, positional encoding 생성
        input_emb = self.input_emb(x)
        pos_encoding = self.pos_encoding(x)
        
        # 2. add & dropout
        x = self.dropout(input_emb + pos_encoding)

        # 3. n 번 EncoderLayer 반복하기
        for encoder_layer in self.encoder_layers:
            x, _ = encoder_layer(x, padding_mask)
        
        return x