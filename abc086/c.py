n=int(input())
points=list()
for i in range(n):
    points.append(list(map(int, input().split())))

t,x,y=(0,0,0)
for point in points:
    t_move, x_move, y_move=(point[0] - t ,point[1] - x, point[2] - y)
    t, x,y=(point[0], point[1], point[2])
    if t<abs(x_move + y_move)\
            or(t_move%2==0 and (x_move+y_move)%2!=0)\
            or(t_move%2!=0 and (x_move+y_move)%2==0):
        break
else:
    print("Yes")
    exit(0)
print("No")
