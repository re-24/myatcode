# 逆から見るパターン
s=input()[::-1]
words = {"dream", "dreamer", "erase", "eraser"}

while len(s)!=0:
    for i in words:
        l = len(i)
        if s[0:l] == i[::-1]:
            s = s[l::]
            break
    else:
        break

print("NO"if len(s)!=0else "YES")