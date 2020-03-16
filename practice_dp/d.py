N,W=map(int, input().split())
w=[None]*10**5
v=[None]*10**9
for i in range(N):
    w[i],v[i]=map(int, input().split())

dp=[[0]*N for _ in range(W+1)]

for i in range(N):
    for sum_w in range(W+1):
        if sum_w >= w[i]:
            dp[i+1][sum_w] = max(dp[i][sum_w-w[i]]+v[i], dp[i][sum_w])
        else:
            dp[i+1][sum_w] = dp[i][sum_w]
print(max(dp[N]))
