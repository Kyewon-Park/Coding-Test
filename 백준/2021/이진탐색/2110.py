#not done

import sys
input = sys.stdin.readline
n,c = map(int,input().split())
coord = [int(input()) for _ in range(n)]
coord.sort()
start = 0
end = max(coord)
minC = min(coord)
while dist<=end:
    dist = (start+end)//2

    a=0 #인덱스
    c=n-1
    b = (a+c)//2    
    while a<=c:
        b = (a+c)//2    
        if minC+dist < coord[b]:
            a=b
        else:
            c=b
    for _ in range(c-1):
        coord[b]
        



