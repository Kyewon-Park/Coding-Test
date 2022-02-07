# 평범한 배낭
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
d = [0]*(k+1)
w = [0]*n
v = [0]*n
for i in range(n):
    w[i],v[i] = map(int,input().split())
for i in range(n):
    for j in range(k,0,-1):
        if w[i]<=j:
            d[j] = max(d[j], d[j-w[i]]+v[i])
print(max(d))    