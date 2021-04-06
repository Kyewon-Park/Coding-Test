INF=int(1e9)
n=6
m=11
start=2
input = [[1,2,2],[1,3,5],[1,4,1],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for i in range(len(input)):
    a,b,c=input[i]
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    #가지 않은, 가장 작은 노드
    for i in range(1,n+1):
        if(distance[i]<min_value and not visited[i]):
            min_value=distance[i]
            node_num=i
        return node_num

def dijkstra(start):
    #출발 노드 설정
    distance[start]=0
    visited[start]=True
    #초기화
    for i in graph[start]:
        distance[i[0]] = i[1]

    for _ in range(n-1):
        #가장 거리 작은 노드
        sn = get_smallest_node()
        #갱신
        visited[sn]=True
        for i in graph[sn]:
            distance[i[0]] = min(distance[sn]+ i[1], distance[i[0]])

dijkstra(start)

for i in range(1,n+1):
    if(distance[i]==INF):
        print("INF")
    else:
        print(distance[i])
