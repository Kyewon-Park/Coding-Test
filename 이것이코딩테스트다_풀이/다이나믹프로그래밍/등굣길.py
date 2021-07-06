def solution(m, n, puddles):
    INF = int(1e9)
    dp=[[0]*(m+1) for i in range(n+1)] 
    for p in puddles:
        dp[p[0]][p[1]]=INF
    dp[1][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(i==1 and j==1 or dp[i][j]==INF):
                continue
            if(i==1):
                up=0
            else:
                up=dp[i-1][j]
            if(j==1):
                left=0
            else:
                left=dp[i][j-1]
            
            if(left==INF and up!=INF):
                dp[i][j]=up
            elif(left!=INF and up==INF):
                dp[i][j]=left
            elif(left!=INF and up!=INF):
                dp[i][j]=left+up
            else"
            
                

            
    print(dp)
    return dp[n][m]

solution(4,3,[[2,2]])