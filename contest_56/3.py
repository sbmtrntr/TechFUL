from math import sqrt
r, R = map(int, input().split())
ans = 0
for x in range(-100, 101):
    for y in range(-100, 101):
        if r <= sqrt(x**2 + y**2) <= R:
            ans += 1
print(ans)