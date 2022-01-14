# 분수찾기 !!!!!
import math
n = int(input()) 
x = math.ceil((math.sqrt(8*n+1)-1)/2)
a=1
b=1
t = (x+1)*x//2 - n
if x%2==1:
    a=1
    b=x    
    for _ in range(t):
        a=a+1
        b=b-1
else:
    a=x
    b=1
    for _ in range(t):
        a=a-1
        b=b+1
print(f"{a}/{b}")