from torch import nn

from model.layers.embedding.positional_encoding import PositionalEncoding
from model.layers.encoder_layer import EncoderLayer

class Encoder(nn.Module):
    def __init__(self, n_input_vocab, d_model, head, d_ff, max_len, padding_idx, dropout, n_layers, device):
        super().__init__()

        # input embedding
        self.input_emb = nn.Embedding(n_input_vocab, d_model, padding_idx=padding_idx)
        self.pos_encoding = PositionalEncoding(d_model, max_len, device)
        self.dropout = nn.Dropout(p=dropout)

        # Add EncoderLayers to the list
        self.encoder_layers = nn.ModuleList([EncoderLayer(d_model=d_model, 
                                                         head=head, 
                                                         d_ff=d_ff, 
                                                         dropout=dropout)
                                             for _ in range(n_layers)])

    def forward(self, x, padding_mask):
        # 1. make input embedding, positional encoding
        # (batch_size, seq_len, d_model)
        input_emb = self.input_emb(x)
        # (seq_len, d_model)
        pos_encoding = self.pos_encoding(x)
        
        # 2. add & dropout
        # (batch_size, seq_len, d_model)
        x = self.dropout(input_emb + pos_encoding)

        # 3. Repeat EncoderLayer n times
        for encoder_layer in self.encoder_layers:
            x, attention_score = encoder_layer(x, padding_mask)
        
        return x