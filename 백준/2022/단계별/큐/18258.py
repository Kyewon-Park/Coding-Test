# 큐2 

import sys
from collections import deque
l = deque([])
print(len(l))
input = sys.stdin.readline
N = int(input().strip())
for _ in range(N):
    i = input().strip()
    if len(i)>5:
        a,b=i.split()
        l.append(b)
    elif i=='pop':
        if len(l)==0:
            print(-1)
        else:   
            print(l.popleft())
    elif i=='empty':
        if len(l)==0:
            print(1)
        else:   
            print(0)
    elif i=='size':
        print(len(l))
    elif i=='front':
        if len(l)==0:
            print(-1)
        else:
            print(l[0])
    elif i=='back':
        if len(l)==0:
            print(-1)
        else:
            print(l[-1])
