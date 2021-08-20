#계단오르기
#다시한번 살펴보기
#계단오르기
import sys
input=sys.stdin.readline
n=int(input())
stair=[0]*(n+1)
for i in range(1,n+1):
    stair[i]=int(input())
d=[0]*(n+1)
d[1]=stair[1]
if(n==1):
    print(d[n])
elif(n==2):
    d[2]=stair[2]+stair[1]
    print(d[n])
else:
    d[2]=stair[2]+stair[1]
    d[3]=max(stair[2]+stair[3],stair[3]+stair[1])
    for i in range(4,n+1):
        d[i]= max(stair[i]+d[i-2], stair[i]+stair[i-1]+d[i-3])
    print(d[n])
