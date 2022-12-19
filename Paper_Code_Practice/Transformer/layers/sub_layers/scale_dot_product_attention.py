import torch
import torch.nn as nn

class ScaleDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax = nn.Softmax(dim=-1) # dim = -1 은 단어들에 해당하는 위치 ([batch_size, head, seq_len, seq_len])
        
    def forward(self, q, k, v, mask=None):
        # q,k,v 의 크기는 같음 
        # [batch_size, head, seq_len, head_dim(기존 d_model을 head 수로 나눈 각 head의 dim)]
        batch_size, head, seq_len, head_dim = q.size()

        # 1. K를 transpose하기 (seq_len, head_dim의 위치 전환)
        k_t = k.transpose(-1,-2)

        # 2. Q 와 K^T 의 MatMul
        attention_score = torch.matmul(q,k_t)
        # attention_score: [batch_size, head, seq_len, seq_len]

        # 3. scale(1/sqrt(d_k == head_dim)) 곱하기
        attention_score /= torch.sqrt(torch.Tensor([head_dim]))

        # 4. Mask가 있다면 해당 부위 -1e10으로 채우기
        if mask:
            attention_score = attention_score.masked_fill(mask==0,-1e10) # Tensor.masked_fill_(mask_boolean, value)
        
        # 5. softmax 취하기 
        attention_score = self.softmax(attention_score)

        # 6. attention 결과값과 V MatMul 계산하기
        result = torch.matmul(attention_score, v)
        
        return result, attention_score