#https://programmers.co.kr/learn/courses/30/lessons/49191
def solution(n, results):
    INF=int(1e9)
    graph=[[INF]*(n+1) for _ in range(n+1)]
    for r in results:
        graph[ r[0] ][ r[1] ]=1
    
    for i in range(1,n+1):
        graph[i][i]=0
        
    for k in range(n+1):
        for i in range(n+1):        
            for j in range(n+1):        
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
                
    ans=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[j][i] == INF and graph[i][j] == INF:
                break
            if(j==n):
                ans.append(i)
                
    return len(ans)