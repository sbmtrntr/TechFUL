a = input()
n = int(input())
ans = []
for i in range(len(a)-n+1):
    ans.append(a[i:i+n])

print(*ans)