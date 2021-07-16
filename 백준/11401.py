#이항계수 3

def factorial(n,until):
    if n==until:
        return until
    return n*factorial(n-1,until)

n,k = map(int, input().split())
top = factorial(n,k+1)
div = factorial(n-k,1)
ans = int(top/div)
print(ans%1000000007)