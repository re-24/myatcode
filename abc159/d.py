from collections import Counter
n=int(input())
a=[int(A) for A in input().split()]

cnt=Counter(a)
s=sum([c*(c-1)//2 for c in cnt.values()])

for k in a:
    print(s-(cnt[k]-1))
