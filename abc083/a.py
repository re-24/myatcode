a,b,c,d = map(int, input().split())
w = (a+b) - (c+d)
if w == 0:
    print("Balanced")
elif w > 0:
    print("Left")
else:
    print("Right")