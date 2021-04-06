import heapq
INF=int(1e9)
n=6
m=11
start=2
input = [[1,2,2],[1,3,5],[1,4,1],[2,3,3],[2,4,2],[3,2,3],[3,6,5],[4,3,3],[4,5,1],[5,3,1],[5,6,2]]

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    a,b,c=input[i]
    graph[a].append((b,c))

def dijkstra2(start):
    #우선순위큐에 담을것
    h = []
    heapq.heappush(h, (0,start)) #거리,위치
    #초기화
    distance[start] = 0

    while(h):
        #get smallest node
        dist, sn = heapq.heappop(h)
        if distance[sn]<dist: #이미 처리된적 있으면
            continue
        #재정렬
        for i in graph[sn]: #i[0]: n번노드  |  i[1]: n번에서부터 distance
            cost = distance[sn]+i[1]
            distance[i[0]] = min(cost, distance[i[0]])
            if(distance[i[0]]==cost):
                heapq.heappush(h,(cost,i[0]))


    