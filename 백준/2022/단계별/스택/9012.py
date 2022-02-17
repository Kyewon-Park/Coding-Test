#괄호

import sys
input = sys.stdin.readline
N = int(input().strip())
for _ in range(N):
    l = list(input().strip().split(')('))
    print(l)
    # up=down=0
    # for i in l:
    #     if i == '(':
    #         up+=1
    #     else:
    #         down+=1
        