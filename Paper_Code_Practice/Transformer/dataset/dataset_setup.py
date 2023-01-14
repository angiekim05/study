import os

if not os.path.exists("dataset/dataset"):
    os.makedirs("dataset/dataset")
if not os.listdir('dataset/dataset') :
    with open("dataset/setup.txt") as f:
        for c in f.readlines():
            os.system(c.strip())