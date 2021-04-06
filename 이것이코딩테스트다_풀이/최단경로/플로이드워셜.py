INF=int(1e9)
n=6
m=11
start=2
input = [[1,2,2],[1,3,5],[1,4,1],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    graph[a][a]=0

for i in input:
    a,b,c = i
    graph[a][b]=c

for k in range(1,n+1): #k번 노드를 거쳐가는 경우
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("X", end =" ")        
        else:
            print(graph[a][b], end=" ")
    print()
