import heapq
n=6
m=7
INF=int(1e9)
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
graph[3].append((6,1))
graph[4].append((3,1))
graph[3].append((2,1))
graph[1].append((3,1))
graph[1].append((2,1))
graph[2].append((4,1))
graph[5].append((2,1))

graph[6].append((3,1))
graph[3].append((4,1))
graph[2].append((3,1))
graph[3].append((1,1))
graph[2].append((1,1))
graph[4].append((2,1))
graph[2].append((5,1))

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    while(q):
        dist, now = heapq.heappop(q)
        if(dist>distance[now]):
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if(cost<distance[i[0]]):
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    print(distance)

dijkstra(1)