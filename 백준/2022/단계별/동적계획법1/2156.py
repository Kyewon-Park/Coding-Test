#포도주 시식
import sys
input=sys.stdin.readline
n = int(input().strip())
l = [int(input().strip()) for _ in range(n)]
d = [0]*(n)
d[0]=l[0]
if n>1:
    d[1]=l[0]+l[1]
if n>2:
    d[2]=max(l[0]+l[2],l[1]+l[2],d[1])
for i in range(3,n):
    d[i] = max(d[i-3]+l[i-1]+l[i], d[i-2]+l[i], d[i-1])
print(d[n-1])