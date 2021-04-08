def solution(m, n, puddles):
    INF = int(1e9)
    d = [[-1] * (n+1) for _ in range(m+1)]
    
    for p in puddles:
        d[p[0]][p[1]]=INF

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(d[i][j]==INF):
                continue
            if(i==1):
                if(d[i][j-1]!=INF):
                    d[i][j] = d[i][j-1]+1
                else:
                    d[i][j]=INF
            elif(j==1):
                if(d[i-1][j]!=INF):
                    d[i][j] = d[i][j-1]+1
                else:
                    d[i][j]=INF
            else:
                if(d[i-1][j]==INF and d[i][j-1]==INF):
                    d[i][j]=INF
                    continue
                d[i][j] = min(d[i-1][j]+1, d[i][j-1]+1)

    return (d[m][n]-1)%1000000007

print(solution(4,3,[[2,2]]))