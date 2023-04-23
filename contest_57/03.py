N, X, Y, Z = map(int, input().split())
movement = [-3, -2, -1, 0, 1, 2, 3]
ans = 0

for i in movement:
    for j in movement:
        for k in movement:
            print((X+i) % N, (Y+j) % N, (Z+k) % N)
            if (X+i) % N == (Y+j) % N == (Z+k) % N:
                ans += 1

print(ans)