items = [
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4)
]

W = int(input("배낭 용량을 입력하세요: "))
n = len(items)

dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    name, wt, val = items[i-1]
    for w in range(1, W + 1):
        if wt <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - wt] + val)
        else:
            dp[i][w] = dp[i-1][w]

print("최대 만족도:", dp[n][W])

selected = []
w = W

for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        name, wt, val = items[i-1]
        selected.append(name)
        w -= wt

selected.reverse()
print("선택된 물건:", selected)
