n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

alice = 0
bob = 0

for i, d in enumerate(a):
    if i%2 == 0:
        alice += d
    else:
        bob += d

print(alice - bob)

