# 패션왕 신해빈
#!!!!!!!!!!!!!!
import sys
input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
    d = dict()
    n = int(input().strip())
    for _ in range(n):
        a,b = input().strip().split()
        if b in d:
            d[b] += 1
        else:
            d[b] = 1
    ans=1
    for v in d.values():
        ans *= (v+1)
    print(ans-1)