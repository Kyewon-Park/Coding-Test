INF=int(1e9)
n=int(input())
graph=[[INF]*(n) for _ in range(n)]
for i in range(n):
    li = list(map(int,input().split()))
    for j in range(n):
        graph[i][j]= li[j]
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b]= max(graph[a][k]+graph[k][b],graph[a][b])
for a in range(n):
    for b in range(n):
        if(graph[a][b]==INF):
            print("0",end=" ")
        else:
            print("1", end=" ")
    print()