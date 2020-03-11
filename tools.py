# 因数分解
def prime_factorization(n):
    if n <= 3: return [n]
    prime=[]
    for i in range(2, int(n**0.5)+1):
        while n%i==0:
            n//=i
            prime.append(i)
    if n!=1:prime.append(n)
    return prime

for i in range(100):
    print(i, prime_factorization(i))
