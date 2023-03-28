N = int(input())
X = [int(x) for x in input().split()]
MIN = int(input())
MAX = int(input())
C = int(input())
haba = (MAX - MIN + 1) // C
counter = [0 for i in range(C)]
for i in range(N):
    for j in range(C):
        if MIN <= X[i] <= MAX and X[i] <= MIN - 1 + haba*(j+1):
            counter[j] += 1
            break
print(counter)