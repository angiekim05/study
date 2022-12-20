import torch
import torch.nn as nn

from layers.sub_layers.scale_dot_product_attention import ScaleDotProductAttention

class MultiHeadAttention(nn.Module):
    def __init__(self,d_model,head):
        super().__init__()
        self.d_model = d_model
        self.head = head
        self.head_dim = d_model // head
        self.w_q = nn.Linear(d_model,d_model)
        self.w_k = nn.Linear(d_model,d_model)
        self.w_v = nn.Linear(d_model,d_model)
        self.w_o = nn.Linear(d_model,d_model)
        self.attention = ScaleDotProductAttention()

    def forward(self, q, k, v, mask=None):
        #  [batch_size, seq_len, d_model]
        batch_size, seq_len, d_model = q.size()
        
        # 1. Q,K,V를  d_k, d_k, d_v 차원으로 projection
        q, k, v = self.w_q(q), self.w_k(k), self.w_v(v)

        # 2. Q,K,V를 head 수 만큼 분리해주기 -> [batch_size, head, seq_len, head_dim]
        q = torch.cat(q.chunk(self.head, dim=-1), dim=0)
        k = torch.cat(k.chunk(self.head, dim=-1), dim=0)
        v = torch.cat(v.chunk(self.head, dim=-1), dim=0)

        # 3. Scaled Dot-Product Attention 을 수행하기
        out, attention = self.attention(q,k,v,mask)

        # 4. 분리된 head들을 concat 하기
        out = torch.cat(out.chunk(self.head,dim=0),dim=-1)

        # 5. d_model 차원으로 projection
        out = self.w_o(out)

        return out, attention