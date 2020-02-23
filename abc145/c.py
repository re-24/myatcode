import math
import itertools

# 入力
n = int(input())
town = dict()
for i in range(n):
    x, y = map(int, input().split())
    town[i] = [x, y]


def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


total = 0
for p in itertools.permutations(town, n):
    bef = p[0]
    for i in p[1:]:
        total += distance(town[bef], town[i])
        bef = i

print(total/math.factorial(n))



