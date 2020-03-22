h, w = map(int, input().split())
hdiv = h // 2
hmod = h % 2
if h==1 or w==1:
    print(1)
elif hmod == 0:
    print(hdiv * w)
else:
    print(hdiv * w + w // 2 + w % 2)