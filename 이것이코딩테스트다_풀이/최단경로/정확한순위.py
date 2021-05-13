n=6 
m=6

INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
graph[1][5]=1
graph[3][4]=1
graph[4][2]=1
graph[4][6]=1
graph[5][2]=1
graph[5][4]=1

#자기자신한테 가는 경로 0
for i in range(1,n+1):
    graph[i][i]=0
#플로이드워셜
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
#그래프에서 INF발견되면 제외
ans=[]
for i in range(1,n+1): #1,2,3..6
    for j in range(1,n+1): 
        if(graph[j][i]==INF and graph[i][j]==INF):
            break
        if(j==n):
            ans.append(i)
    
print(graph)
print(ans)
    
