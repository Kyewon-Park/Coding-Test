INF=int(1e9)
n=5
m=7
input=[[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5]]
start=1
x=4
k=5

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for i in input:
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1

for k in range (1,n+1):
    for i in range (1,n+1):
        for j in range (1,n+1):
            graph[i][j] = min(graph[i][k]+graph[k][j], graph[i][j])

for a in graph:
    for b in a:
        if(b>=INF):
            print('I',end=" ")
        else:
            print(b,end=" ")
    print()

print(graph[1][k])
print(graph[k][x])
dist=graph[1][k]+graph[k][x]
if(dist>=INF):
    print('-1',end=" ")
else:
    print(f"min ={dist}")