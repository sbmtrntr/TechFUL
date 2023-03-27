N = int(input())
for _ in range(7):
    temp = str(N**2)
    temp = '0'*(12 - len(temp)) + temp
    N = int(temp[3:9])
    print(N % 6 + 1)