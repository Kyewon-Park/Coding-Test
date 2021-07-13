#MooTube
INF = int(1e9)
N, Q= map(int,input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    graph[i][i]=0


for _ in range(N-1):
    p,q,r = map(int,input().split())
    graph[p][q]=r
    graph[q][p]=r

for a in range(1,N+1):
    for b in range(1,N+1):
        if(a>=b):
            continue
        for k in range(1,N+1):
            if(graph[a][k]!=INF and graph[k][b]!=INF and graph[k][b]!=0 and graph[a][k]!=0):
                graph[a][b]= min(graph[a][k],graph[k][b])

kvs=[]
for i in range(Q):
    k, v= map(int,input().split())
    kvs.append((k,v))

for k,v in kvs:
    count=0
    for j in graph[v]:
        if(j>=k):
            count+=1
    print(count-1)