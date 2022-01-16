# Fly me to the Alpha Centauri

import math
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    l = b-a
    x = math.floor(math.sqrt(l))
    if(l==1):
        print(1)
    elif l == x*x:
        print(2*x-1)
    elif l <= x*x + x:
        print(2*x)
    else:
        print(2*x+1)