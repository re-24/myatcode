N,W=map(int, input().split())
w=[None]*100
v=[None]*100
for i in range(N):
    w[i],v[i]=map(int, input().split())

dp=[[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for weight in range(W+1):
        if weight - w[i] >= 0:
            dp[i+1][weight] = max(dp[i][weight-w[i]]+v[i], dp[i][weight])
        else:
            dp[i+1][weight] = dp[i][weight]
print(max(dp[N]))
