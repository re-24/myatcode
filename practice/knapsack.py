N,WEIGTH = map(int, input().split())
v=list()
w=list()
for i in range(N):
    tmp = input().split()
    v.append(int(tmp[0]))
    w.append(int(tmp[1]))

dp = [[-1 for i in range(WEIGTH+1)] for j in range(N+1)]
for i in range(WEIGTH+1):
    dp[0][i]=0
print(dp)
for idx in range(N):
    for weight in w:
        dw, dv = dp[idx]
        if WEIGTH >= dw + weight:
            dp.append(dw+weight, max(dv + v[idx]))
        else:
            dp.append(dw, dv)

