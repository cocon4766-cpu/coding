import numpy as np 

W = 0.0
learning_rate = [0.01,0.1,0.5]
for lr in learning_rate:
    print(f"\n---- Testing Learning Rate: {lr} ----")
    W = 0.0
    for i in range(1,11):
        loss = (W-5)**2
        gradient = 2*(W-5)
        W = W -lr*gradient
        print(f"layer{i}: weights = {W:.4f} loss = {loss:.4f}, gradient = {gradient:.4f}")