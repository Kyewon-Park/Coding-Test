#설탕 배달
INF=99999
dp=[INF]*5001
dp[3]=1
dp[5]=1
for i in range(6,5001):
    if dp[i-3]==-1 and dp[i-5]==-1:
        continue
    dp[i]=min(dp[i-3]+1,dp[i-5]+1)
print(dp[int(input())])