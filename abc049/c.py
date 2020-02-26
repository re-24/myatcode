s = input()
t = ""

p = 0
while p < len(s):
    if s[p:p+5] == 'dream' and s[p+5:p+6] != 'e':
        p += 5
        t += 'dream'
    elif s[p:p+5] == 'erase' and s[p+5:p+6] != 'r':
        p += 5
        t += 'erase'
    elif s[p:p+6] == 'eraser':
        p += 6
        t += 'eraser'
    elif s[p:p+7] == 'dreamer' and s[p+7:p+8] != 'a':
        p += 7
        t += 'dreamer'
    elif s[p:p+7] == 'dreamer' and s[p+7:p+8] == 'a':
        p += 5
        t += 'dream'
    else:
        break

print("YES" if t==s else "NO")


