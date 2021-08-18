#퇴사
import sys
input=sys.stdin.readline
n=int(input())
T=[]
P=[]
for _ in range(n):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)
dp=[0]*(n+1)
maxV=0
for i in range(n-1,-1,-1):
    if T[i]+i>n:
        dp[i]=maxV
    else:
        dp[i]=max(P[i]+dp[i+T[i]],maxV)
        maxV=dp[i]
print(dp[0])
