n = int(input())

### member_listの初期化
member_list = [[0 for j in range(4)] for i in range(n)]

### 入力をmember_listに代入
### 「データレコード」とは異なる入力形式であることに注意してください
for i in range(n):
    member_list[i] = input().split()

### 操作の入力
operation = input()

### 操作がconcatの場合
if operation == "concat":
    for i in range(n):
        ### 新たなデータの結合
        member_list[i].append(input())
        ### 結合後のデータの出力
        print(*member_list[i])

### 操作がdeleteの場合
elif operation == "delete":
    ### 削除する名前(name_del)の代入
    name_delete = input()
    ### 名前の検索
    for i in range(n):
        if member_list[i][0] == name_delete:
            member_list.pop(i)
            break
    ### 削除後のデータの出力
    for i in range(n-1):
        print(*member_list[i])