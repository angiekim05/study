from torch import nn

from model.layers.embedding.positional_encoding import PositionalEncoding
from model.layers.decoder_layer import DecoderLayer

class Decoder(nn.Module):
    def __init__(self, n_output_vocab, d_model, head, d_ff, max_len, padding_idx, dropout, n_layers, device):
        super().__init__()

        # output embbeding 
        self.output_emb = nn.Embedding(n_output_vocab, d_model, padding_idx=padding_idx)
        self.pos_encoding = PositionalEncoding(d_model, max_len, device)
        self.dropout = nn.Dropout(p=dropout)

        # Add DecoderLayers to the list
        self.decoder_layers = nn.ModuleList([DecoderLayer(d_model=d_model, 
                                                         head=head, 
                                                         d_ff=d_ff, 
                                                         dropout=dropout)
                                             for _ in range(n_layers)])

    def forward(self, x, memory, look_ahead_mask, padding_mask):
        # 1. make input embedding, positional encoding
        # (batch_size, seq_len, d_model)
        output_emb = self.output_emb(x) 
        # (seq_len, d_model)
        pos_encoding = self.pos_encoding(x) 
        
        # 2. add & dropout
        # (batch_size, seq_len, d_model)
        x = self.dropout(output_emb + pos_encoding) 

        # 3. Repeat DecoderLayer n times
        for decoder_layer in self.decoder_layers:
            x = decoder_layer(x, memory, look_ahead_mask, padding_mask)

        return x