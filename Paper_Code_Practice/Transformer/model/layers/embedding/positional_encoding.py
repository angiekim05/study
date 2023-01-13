import torch
from torch import nn

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len, device):
        super().__init__()

        # Positional Encoding 초기화
        # 1. 비어있는 tensor 생성
        # (max_len,d_model)
        self.P_E = torch.zeros(max_len, d_model, device=device)
        # 학습되는 값이 아님으로 requires_grad 을 False로 설정
        self.P_E.requires_grad = False

        # 2. pos (0~max_len) 생성 (row 방향 => unsqueeze(dim=1))
        pos = torch.arange(0, max_len, dtype=torch.float, device=device).unsqueeze(dim=1)

        # 3. _2i (0~2i) 생성 (col 방향)
        # 2i는 step = 2 를 활용하여 i의 2배수를 만듦
        _2i = torch.arange(0, d_model, step= 2, dtype=torch.float, device=device)

        # 4. 제안된 positional encoding 생성 
        # (i가 짝수일때 : sin, 홀수일때 : cos)
        self.P_E[:, 0::2] = torch.sin(pos / 10000 ** (_2i / d_model))
        self.P_E[:, 1::2] = torch.cos(pos / 10000 ** (_2i / d_model))

    def forward(self,x):
        # x seq 길이에 맞춰 PE return 
        # (seq_len, d_model)
        batch_size, seq_len = x.size()
        PE_for_x = self.P_E[:seq_len,:]

        return PE_for_x