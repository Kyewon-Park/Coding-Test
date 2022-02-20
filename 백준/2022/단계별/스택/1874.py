# 스택 수열

from collections import deque
import sys
input = sys.stdin.readline
N = int(input().strip())
l = []
for _ in range(N):
    l.append(int(input().strip()))
l = deque(l)
nl = deque(sorted(l))

poppedl = []
ans=[]

while(True):
    if len(nl)==0:
        if len(l)==0:
            break
        popped = poppedl.pop()
        if popped == l[0]:
            ans.append('-')
            l.popleft()
        else:
            ans=['NO']
            break
    elif nl[0]>l[0]:
        popped = poppedl.pop()
        if popped != l.popleft():
            ans=['NO']
            break
        else:
            ans.append('-')
    else:
        np = nl.popleft()
        ans.append('+')
        if l[0] == np:
            l.popleft()
            ans.append('-')
        else:
            poppedl.append(np)

for i in ans:
    print(i)