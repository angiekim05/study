from torch import nn

class PositionWiseFCFeedForwardNetwork(nn.Module):
    def __init__(self,d_model,d_ff):
        super().__init__()
        self.w_1 = nn.Linear(d_model,d_ff)
        self.relu = nn.ReLU()
        self.w_2 = nn.Linear(d_ff,d_model)
    
    def forward(self, x):
        # Linear Layer1
        x = self.w_1(x)

        # ReLU
        x = self.relu(x)
        
        # Linear Layer2
        x = self.w_2(x)

        return x