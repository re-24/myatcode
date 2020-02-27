import time

def fib(n):
    if n==0:return 0
    if n==1:return 1
    return fib(n-1)+fib(n-2)

done = dict()
memo = dict()
def fib_memo(n):
    if n==0:return 0
    if n==1:return 1
    if done.get(n): return memo[n]
    done[n] = True
    memo[n] = fib_memo(n-1)+fib_memo(n-2)
    return memo[n]

n = 990
# current_time = time.time()
# fib(n)
# print(time.time()-current_time)

current_time = time.time()
print([fib_memo(i) for i in range(n)])
print(time.time()-current_time)