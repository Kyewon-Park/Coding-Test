#DFS와 BFS
import sys
from collections import deque
input=sys.stdin.readline
n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()
#DFS
visited = [False]*(n+1)
def dfs(graph, now, visited):
    visited[now]=True
    print(now, end=" ")
    for i in graph[now]: #2,3,6
        if not visited[i]:
            dfs(graph,i,visited)
dfs(graph,start,visited)
print()
#BFS
visited = [False]*(n+1)
queue = deque([start])
visited[start]=True
while queue:
    now=queue.popleft()
    print(now,end=" ")
    for i in graph[now]:
        if not visited[i]:
            queue.append(i)
            visited[i]=True