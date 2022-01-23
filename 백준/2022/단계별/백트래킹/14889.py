#스타트와 링크
from itertools import combinations, permutations
import sys
input = sys.stdin.readline
n=int(input().strip())
l=[]
s=0
for _ in range(n):
    li=list(map(int, input().strip().split()))
    s+=sum(li)
    l.append(li)
m=n//2
lc = list(combinations(range(1,n+1),m))
nlc = len(lc)
min=99999
for i in range(nlc//2):
    pl = list(permutations(lc[i],2))
    lsi=0
    for j in pl:
        lsi+=l[j[0]-1][j[1]-1]
    pr = list(permutations(lc[nlc-i-1],2))
    rsi=0
    for j in pr:
        rsi+=l[j[0]-1][j[1]-1]

    ans = abs(lsi-rsi)
    if min>ans:
        min=ans
print(min)