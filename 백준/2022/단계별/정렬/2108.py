#통계학
from collections import Counter
import sys
input = sys.stdin.readline
n=int(input())
l=[]
for _ in range(n):
    l.append(int(input()))
l.sort()
print(round(sum(l)/n))
print(l[n//2])
cl = Counter(l).most_common(2)
if n>1 and cl[0][1] == cl[1][1]:
    print(cl[1][0])
else:
    print(cl[0][0])
print(l[-1]-l[0])