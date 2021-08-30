import sys
input=sys.stdin.readline
n=int(input())
d=[1]*(101)
d[4]=2
d[5]=2
for i in range(6,101):
    d[i]=d[i-5]+d[i-1]
for _ in range(n):
    x=int(input())
    print(d[x])