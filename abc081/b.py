n = int(input())
a = map(int, input().split())
cnt = 0


def half(_a):
    ret = list()
    for i in _a:
        if i % 2 != 0:
            return None
        else:
            ret.append(i//2)
    return ret


while True:
    a = half(a)
    if not a:
        break
    cnt += 1

print(cnt)

