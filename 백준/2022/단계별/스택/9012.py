#괄호

import sys
input = sys.stdin.readline
N = int(input().strip())
for _ in range(N):
    stk=[]
    l = list(input().strip())
    n = len(l)
    for i in range(n):
        stk.append(l[i])
        if l[i]=='(':
            continue
        elif len(stk)>1 and l[i]==')':
            stk.pop()
            stk.pop()
        else:
            break
    if len(stk)==0:
        print('YES')
    else:
        print('NO')

