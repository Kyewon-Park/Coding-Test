dp = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
n = 5

for i in range(1,n):
    for j in range(i+1):
        #왼쪽 위에서 내려오는 경우
        if(j==0):
            up_left=0
        else:
            up_left=dp[i-1][j-1]
        #바로 위에서 내려오는 경우
        if(j==i):
            up=0
        else:
            up=dp[i-1][j]

        dp[i][j] = max(up,up_left) + dp[i][j]

print(dp)