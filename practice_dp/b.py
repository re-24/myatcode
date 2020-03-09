# https://atcoder.jp/contests/dp/tasks/dp_b
import sys
input = sys.stdin.readline  # これ使うと早いらしい

n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = list()  # もらうDPで解く場合は、1要素目だけ初期化すれば良い
dp.append(0)

# もらうDPに書き換え
for i in range(1, n):
    dp.append(min(
        dp[j] + abs(h[j] - h[i]) for j in range(max(i - k, 0), i)
    ))
print(dp[-1])