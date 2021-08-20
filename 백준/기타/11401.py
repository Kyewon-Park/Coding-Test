n, k = map(int, input().split())
mod = 1000000007
fact = [1 for _ in range(n+1)]

for i in range(2,n+1):
    fact[i]=fact[i-1]*i

