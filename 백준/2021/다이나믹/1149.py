import sys
input=sys.stdin.readline
n=int(input())
houses=[[] for _ in range(n)]
for i in range(n):
    houses[i] = list(map(int,input().split()))
dp=[[0]*3 for _ in range(n)]
dp[0]=houses[0]
for i in range(1,n):
    dp[i][0]=max(dp[i-1][1],dp[i-1][2])+houses[i][0]
    dp[i][1]=max(dp[i-1][0],dp[i-1][2])+houses[i][1]
    dp[i][2]=max(dp[i-1][0],dp[i-1][1])+houses[i][2]
print(dp[n])
