import torch

# GPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

batch_size = 128

# model parameter
n_layers = 6
d_model = 512
d_ff = 2048
head = 8
dropout = 0.1
max_len = 150  # 최대 seq 길이로 PE 초기 크기 설정에 쓰임
padding_idx = 1

# optimizer parameter
init_lr = 1e-5
beta1 = 0.9
beta2 = 0.98
eps = 1e-9
weight_decay = 0
warmup_steps = 4000

# run model parameter
clip = 0.5
log_interval = 50
epoch = 1000
inf = float('inf')