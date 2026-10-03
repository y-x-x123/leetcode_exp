import sys
import json
import numpy as np

data = json.loads(sys.stdin.readline().strip())

train = data['train']
test = data['test']

dim = len(train[0][0])

w = np.zeros(dim+1)

lr = 1.0
epoches = 10

for _ in range(epoches):
    for x, y in train:
        y_true = 1 if y==1 else -1

        x = np.array([1]+x, dtype=float)

        score = np.dot(w,x)

        y_pred = 1 if score >=0 else -1

        if y_pred != y_true:
            w = w + lr * y_true * x

res = []

for x in test:
    x = np.array([1]+x, dtype=float)
    score = np.dot(w,x)
    y_pred = 1 if score >= 0 else -1

    res.append(1 if y_pred == 1 else 0)
print(json.dumps(res))





