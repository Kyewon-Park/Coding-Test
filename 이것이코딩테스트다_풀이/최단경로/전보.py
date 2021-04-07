INF=int(1e9)
n,m,start = map(int,input().split())
distance = [INF]*(n+1)
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    node = 0
    for i in range(len(distance)):
        if min_value>distance[i] and visited[i]==False:
            node=i
    return node

def dijkstra(start):
    distance[start]=0
    for i in graph[start]:
        distance[i[0]]=i[1]

    for i in range(n-1):
        sn = get_smallest_node()
        for i in graph[sn]:
            distance[i[0]] = min(distance[i[0]], distance[sn]+i[1])

dijkstra(start)
print(distance)
count=0
max_time=0
for i in distance:
    if i < INF:
        count+=1
        max_time=max(max_time,i)
print(count-1,max_time)       