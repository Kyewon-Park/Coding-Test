#피보나치 함수
import sys
input= sys.stdin.readline
t=int(input())
d=[(0,0)]*(41)
d[0]=(1,0)
d[1]=(0,1)
for i in range(2,41):
    d[i]=(d[i-1][0]+d[i-2][0],d[i-1][1]+d[i-2][1])
for _ in range(t):
    n = int(input())
    print(f"{d[n][0]} {d[n][1]}")
        

