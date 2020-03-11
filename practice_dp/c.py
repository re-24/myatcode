dp=[[0]*3 for _ in range(10**5+1)]
n=int(input())
abc=[[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    dp[i + 1][0] = abc[i][0] + max(dp[i][1], dp[i][2])
    dp[i + 1][1] = abc[i][1] + max(dp[i][0], dp[i][2])
    dp[i + 1][2] = abc[i][2] + max(dp[i][0], dp[i][1])
print(max(dp[n]))

