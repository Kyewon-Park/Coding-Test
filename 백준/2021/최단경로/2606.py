#바이러스
import heapq
import sys
input = sys.stdin.readline

INF=int(1e9)
n=int(input())
m=int(input())
start = 1
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

q=[]
heapq.heappush(q,(start,0))
distance[start]=0
while q:
    now, dist = heapq.heappop(q)
    if distance[now]<dist:
        continue
    for i in graph[now]: #i: [(b,1),(c,1)]
        cost = dist+i[1]
        if distance[i[0]]>cost:
            distance[i[0]]=cost
            heapq.heappush(q,(i[0],cost))

count=0
for i in distance[2:]:
    if i!=INF:
        count+=1
print(count)