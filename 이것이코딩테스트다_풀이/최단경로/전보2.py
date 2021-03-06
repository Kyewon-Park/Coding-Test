import heapq

INF=int(1e9)
n,m,start = map(int,input().split())
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start]=0
    h = []
    heapq.heappush(h,(0,start))
    while h:
        dist,now = heapq.heappop(h)
        if(distance[now] < dist):
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(h, (cost,i[0]))

dijkstra(start)

for d in distance:
    print(d)

