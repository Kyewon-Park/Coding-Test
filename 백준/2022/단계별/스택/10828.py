#스택
import sys
input = sys.stdin.readline
N = int(input().strip())
l = []
for _ in range(N):
    s = input().strip()
    if len(s)>5:
        a, b = s.split()
        l.append(int(b))
    elif s == 'top':
        if len(l)==0:
            print(-1)
        else:
            print(l[-1])
    elif s == 'size':
        print(len(l))
    elif s == 'empty':
        if len(l)==0:
            print(1)
        else:
            print(0)
    else:
        if len(l)==0:
            print(-1)
        else:
            print(l.pop(-1))