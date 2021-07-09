import heapq
import sys

input = sys.stdin.readline
INF=int(1e9)

#start 에서 각 노드로의 최단거리 구하기
n,m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        #가장짧은거리의 노드 뽑아
        dist,now = heapq.heappop()
        if distance[now]<dist:
            continue
        for i in graph[now]: #(노드,거리)
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))