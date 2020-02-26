n, y = map(int, input().split())
y/=1000
for i in range(n+1):
    for j in range(n-i+1):
        k = n-i-j
        if 10*i+5*j+k==y:
            print(i,j,k)
            exit()
print(-1,-1,-1)






