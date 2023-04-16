import numpy as np
import csv

N = 10000

X = []
Y = []

filename = 'data.csv'
flag = True
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    

for i in range(5):
    ans = str(round(np.corrcoef(X[i], Y)[0][1], 2))
    if len(ans) >= 4:
        print(ans)
    else:
        print(ans + '0')