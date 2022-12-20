import torch.nn as nn

class PositionWiseFeedForward(nn.Module):
    def __init__(self,d_model,d_ff):
        super().__init__()
        self.w_1 = nn.Linear(d_model,d_ff)
        self.w_2 = nn.Linear(d_ff,d_model)
    
    def forward(self, x):
        # Linear Layer2 (ReLU ( Linear Layer1 (x) ))
        out = self.w_2(nn.ReLU(self.w_1(x)))

        return out