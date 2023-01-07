from torch import nn

from model.layers.sub_layers.multi_head_attention import MultiHeadAttention
from model.layers.sub_layers.position_wise_ffn import PositionWiseFCFeedForwardNetwork

class EncoderLayer(nn.Module):
    def __init__(self, d_model, head, d_ff, dropout):
        super().__init__()
        self.attention = MultiHeadAttention(d_model,head)
        self.layerNorm1 = nn.LayerNorm(d_model)

        self.ffn = PositionWiseFCFeedForwardNetwork(d_model,d_ff)
        self.layerNorm2 = nn.LayerNorm(d_model)

        self.dropout = nn.Dropout(p=dropout)

    def forward(self, x, padding_mask):
        # 1. multi-head attention
        residual = x  # residual connection을 위해 잠시 담아둠
        x, attention_score = self.attention(q=x, k=x, v=x, mask=padding_mask) 
        
        # 2. add & norm
        x = self.dropout(x) + residual
        x = self.layerNorm1(x)

        # 3. position-wise fc feed-forward network
        residual = x
        x = self.ffn(x)

        # 5. add & norm
        x = self.dropout(x) + residual
        x = self.layerNorm2(x)

        return x, attention_score 