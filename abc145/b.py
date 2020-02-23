n = int(input())
s = input()

target = s[0:n//2]

if s[0:n//2] == s[n//2:]:
    print("Yes")
else:
    print("No")
