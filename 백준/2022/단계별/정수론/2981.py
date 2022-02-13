#검문
import sys
import math

input = sys.stdin.readline
n = int(input().strip())
l = [int(input().strip()) for _ in range(n)]
ans =''
pl=[]
for i in range(1, n):
    pl.append(l[i] - l[i-1])

def div(x):
    div_list = [x]
    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            div_list.append(i)
            if x//i != i:
                div_list.append(x//i) 
    div_list.sort()
    return div_list 

g = math.gcd(*pl)
print(*div(g))
