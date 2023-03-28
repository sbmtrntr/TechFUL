# Python3で解答コードを記入してください
a = input()
ans = []
for i in range(len(a)-1):
    ans.append(a[i]+a[i+1])
print(*ans)