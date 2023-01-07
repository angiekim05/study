import torch
from torch import nn

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len, device):
        super().__init__()

        # self.P_E는 [max_len,d_model]로 초기화 -> 입력 seq 길이에 따라 잘라서 사용 
        # (여러번 생성할 필요 없음)
        self.P_E = torch.zeros(max_len, d_model, device=device)
        # 학습되는 값이 아님으로 requires_grad 을 False로 설정
        self.P_E.requires_grad = False
    
        # 문자 시퀀스의 위치 순서 (row => 2d)
        pos = torch.arange(0, max_len, dtype=torch.float, device=device).unsqueeze(dim=1)

        # d_model 차원을 채울 i 값 (col)
        # 2i는 step = 2 를 활용하여 i의 2배수를 만듦
        _2i = torch.arange(0, d_model, step= 2, dtype=torch.float, device=device)

        # 제안된 positional encoding 생성
        self.P_E[:, 0::2] = torch.sin(pos / 10000 ** (_2i / d_model))
        self.P_E[:, 1::2] = torch.cos(pos / 10000 ** (_2i / d_model))

    def forward(self,x):
        # x seq 길이에 맞춰 PE 크기 조절 [seq_len, d_model]
        batch_size, seq_len = x.size()
        PE_for_x = self.P_E[:seq_len,:]

        return PE_for_x