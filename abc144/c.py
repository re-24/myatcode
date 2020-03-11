n=int(input())
x,y=(1,1)
m=10**12+1
for i in range(1, int(n**0.5)+1):
    x+=1
    if n%x==0: y=n//x
    if n==x*y and m>x+y-2:
        m=x+y-2

if m==10**12+1:
    m=n-1
print(m)


