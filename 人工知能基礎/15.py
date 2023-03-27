n = int(input())

### n人の名前、年齢、身長、体重のデータを格納するmember_listの初期化
member_list = [[0 for j in range(4)] for i in range(n)]

### 入力をmember_listに代入
for i in range(4):
    for j in range(n):
        member_list[j][i] = input()

### データの出力
for i in range(n):
    print(*member_list[i])
