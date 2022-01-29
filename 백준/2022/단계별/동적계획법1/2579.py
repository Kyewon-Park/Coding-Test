#계단오르기
#!!!!!!!!!!!!
import sys
input = sys.stdin.readline
n = int(input().strip())
l=[0]*301
d=[0]*301
for i in range(1,n+1):
    l[i] = int(input().strip())
d[0]=0
d[1]=l[1]
d[2]=l[1]+l[2]
for i in range(3, n+1):
    d[i] = max(d[i-3]+l[i-1]+l[i], d[i-2]+l[i])
print(d[n])