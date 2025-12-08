def knapsack(W, n, wt, val, name):
    tb = []
    for i in range(n + 1):
        line = []
        for j in range(W + 1):
            line.append(0)
        tb.append(line)

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] > w:
                tb[i][w] = tb[i-1][w]
            else:
                a = tb[i-1][w]                 
                b = val[i-1] + tb[i-1][w - wt[i-1]] 

                if b > a:
                    tb[i][w] = b
                else:
                    tb[i][w] = a

    maxv = tb[n][W]

    pick = []
    w = W
    for i in range(n, 0, -1):
        if tb[i][w] != tb[i-1][w]:
            pick = [name[i-1]] + pick
            w = w - wt[i-1]

    return maxv, pick

item_name = ["노트북", "카메라", "책", "옷", "휴대용 충전기"]
item_wt = [3, 1, 2, 2, 1]
item_val = [12, 10, 6, 7, 4]

n = len(item_wt)

W = int(input("배낭 용량을 입력하세요 : "))

res_val, res_pick = knapsack(W, n, item_wt, item_val, item_name)

print("최대 만족도:", res_val)
print("선택된 물건:", res_pick)