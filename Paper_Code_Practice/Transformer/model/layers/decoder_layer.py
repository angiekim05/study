from torch import nn

from model.layers.sub_layers.multi_head_attention import MultiHeadAttention
from model.layers.sub_layers.position_wise_ffn import PositionWiseFCFeedForwardNetwork

class DecoderLayer(nn.Module):
    def __init__(self, d_model, head, d_ff, dropout):
        super().__init__()
        self.attention1 = MultiHeadAttention(d_model,head)
        self.layerNorm1 = nn.LayerNorm(d_model)
        
        self.attention2 = MultiHeadAttention(d_model,head)
        self.layerNorm2 = nn.LayerNorm(d_model)

        self.ffn = PositionWiseFCFeedForwardNetwork(d_model,d_ff)
        self.layerNorm3 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(p=dropout)

    def forward(self, x, memory, look_ahead_mask, padding_mask):
        # 1. masked multi-head attention
        residual = x
        x, _ = self.attention1(q=x, k=x, v=x, mask=look_ahead_mask)

        # 2. add & norm
        x = self.dropout(x) + residual
        x = self.layerNorm1(x)

        # 3. multi-head attention (encoder-decoder attention)
        residual = x
        x, _ = self.attention2(q=x, k=memory, v=memory, mask=padding_mask)

        # 4. add & norm
        x = self.dropout(x) + residual
        x = self.layerNorm2(x)

        # 5. position-wise fc feed-forward network
        residual = x
        x = self.ffn(x)

        # 6. add & norm
        x = self.dropout(x) + residual
        x = self.layerNorm3(x)

        return x 