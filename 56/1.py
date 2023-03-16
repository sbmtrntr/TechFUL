G = [input() for _ in range(6)]
h, w = map(int, input().split())
if G[h-1][w-1] == 'o':
    print('Yes')
else:
    print('No')