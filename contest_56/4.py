import copy
H, W, K = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(map(int, input().split())))

G = [[0 for _ in range(W)] for _ in range(H)]

for _ in range(K):
    for i in range(H):
        for j in range(W):
            if i == 0:
                if j == 0:
                    G[i][j] = (S[i+1][j] + S[i][j+1]) % 2
                elif j == W-1:
                    G[i][j] = (S[i+1][j] + S[i][j-1]) % 2
                else:
                    G[i][j] = (S[i+1][j] + S[i][j+1] + S[i][j-1]) % 2
            elif i == H-1:
                if j == 0:
                    G[i][j] = (S[i-1][j] + S[i][j+1]) % 2
                elif j == W-1:
                    G[i][j] = (S[i-1][j] + S[i][j-1]) % 2
                else:
                    G[i][j] = (S[i-1][j] + S[i][j+1] + S[i][j-1]) % 2
            else:
                if j == 0:
                    G[i][j] = (S[i-1][j] + S[i][j+1] + S[i+1][j]) % 2
                elif j == W-1:
                    G[i][j] = (S[i-1][j] + S[i][j-1] + S[i+1][j]) % 2
                else:
                    G[i][j] = (S[i-1][j] + S[i][j+1] + S[i][j-1] + S[i+1][j]) % 2
    
    S = copy.deepcopy(G)
    
for a in S:
    print(*a)