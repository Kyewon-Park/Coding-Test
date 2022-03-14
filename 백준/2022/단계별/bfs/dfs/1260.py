from collections import deque
import sys

def bfs(graph, v, visited):
    route = deque([v])
    visited[v]=True
    while(route):
        popped = route.popleft()
        print(popped, end=' ')
        for i in graph[popped]:
            if not visited[i]:
                route.append(i)
                visited[i]=True

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

input=sys.stdin.readline
n,m,v = map(int, input().strip().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):    
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)
graph = list(map(sorted, graph))
visited = [False]*len(graph)
dfs(graph,v,visited)
print()
visited = [False]*len(graph)
bfs(graph,v,visited)