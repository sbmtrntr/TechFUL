import random

seed, rand_min, rand_max = map(int, input().split())
### 以下にコードを入力してください。(ヒント： for i in range(5): で 同じ処理を5回繰り返すことができます。)
random.seed(seed)
ans = [random.randint(rand_min, rand_max) for _ in range(5)]
print(*ans)
### ここまで