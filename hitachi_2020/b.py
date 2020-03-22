a,b,m=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
tickets=list()
for i in range(m):
    tickets.append(list(map(int,input().split())))

price_min=float("INF")
for ticket in tickets:
    price = A[ticket[0]-1] + B[ticket[1]-1] - ticket[2]
    price_min = price if price_min>price else price_min

# 割引券を使わない場合
no_ticket=min(A)+min(B)
if price_min > no_ticket: price_min=no_ticket
print(price_min)