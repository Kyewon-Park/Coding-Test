import heapq
import sys

# # 베이스 코드 연습
# INF=int(1e9)
# input-sys.stdin.readline

# n,m=map(int,input().split())
# start=int(input())
# graph=[[] for i in range(n+1)]
# distance=[INF]*(n+1)

# for _ in range(m):
#     a,b,c=map(int,input().split())
#     graph[a].append((b,c))

# def dijkstra(start):
#     q=[] #방문하지 않은 노드들 중 최단거리 순 노드 저장
#     heapq.heappush(q,(0,start)) #initialize
#     distance[start]=0
#     while q:
#         dist,now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]: 
#             cost=dist+i[1]
#             if cost<distance[i[0]]:
#                 distance[i[0]]=cost
#                 heapq.heappush(q,(cost,i[0]))        

