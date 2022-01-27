#파도반 수열
import sys
n = int(sys.stdin.readline().strip())
d=[1]*101
d[4]=2
d[5]=2
for i in range(6,101):
        d[i]=d[i-1]+d[i-5]
for _ in range(n):
    m = int(sys.stdin.readline().strip())
    print(d[m])