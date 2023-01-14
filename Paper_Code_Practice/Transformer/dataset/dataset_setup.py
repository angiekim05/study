import os

if not os.path.exists("data/dataset"):
    os.makedirs("data/dataset")
if not os.listdir('data/dataset') :
    with open("data/setup.txt") as f:
        for c in f.readlines():
            os.system(c.strip())