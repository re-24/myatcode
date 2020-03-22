N,W=map(int, input().split())
w=[None]*100
v=[None]*100
for i in range(N):
    w[i],v[i]=map(int, input().split())

dp=[[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    dp[i+1] = dp[i].copy()
    for j in range(w[i], W+1):
        dp[i+1][j] = max(dp[i][j-w[i]] + v[i], dp[i][j])
    print(dp[i], dp[i + 1])
print(max(dp[N]))
