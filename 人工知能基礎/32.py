n = int(input())

### member_listの初期化
member_list = [[0 for j in range(4)] for i in range(n)]

### 入力をmember_listに代入
for i in range(n):
    member_list[i] = input().split()
    ### 平均値や中央値など数値計算のため、int型に変更
    member_list[i][1:] = list(map(int,member_list[i][1:]))

operation = input()

### 欠損値(-1)の検索
for i in range(n):
    if -1 in member_list[i]:
        idx = 0
        for num in member_list[i]:
            if num == -1:
                break
            idx += 1
        break

### 操作がmeanの場合    
if operation == "mean":
    #他のデータの平均値を欠損値として補完(ヒントを基に)
    mean = 0
    for i in range(n):
        if member_list[i][idx] != -1:
            mean += member_list[i][idx]
    mean //= (n-1)
### 操作がmedianの場合
if operation == "median":
    ### 他のデータの中央値を欠損値として補完(ヒントを基に)
    List = []
    for i in range(n):
        if member_list[i][idx] != -1:
            List.append(member_list[i][idx])
    List.sort()
    if (n-1) % 2 == 0:
        median = (List[(n-1)//2 - 1] + List[(n-1)//2]) // 2
    else:
        median = List[(n-1) // 2]

#操作後のデータを出力
for i in range(n):
    for j in range(4):
        if member_list[i][j] != -1:
            print(member_list[i][j], end = " ")
        else:
            if operation == "mean":
                print(mean, end = " ")
            else:
                print(median, end = " ")
    print()