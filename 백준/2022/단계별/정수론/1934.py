#최소공배수
# import math
import sys
input = sys.stdin.readline

def gcf(x,y):
    while(True):
        r = x%y
        if r==0:
            break
        x = y
        y = r
    return y

def lcm(x,y,gcf):
    return (x*y)//gcf

n = int(input().strip())
for _ in range(n):
    a, b =map(int, input().strip().split())
    # print(math.lcm(a,b))
    print(lcm(a,b,gcf(a,b)))