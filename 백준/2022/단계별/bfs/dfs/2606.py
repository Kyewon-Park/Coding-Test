#바이러스

from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

spread = deque([1])
visited=[False]*(n+1)
count=0
while(spread):
    now = spread.popleft()
    for i in graph[now]:
        if not visited[i]:
            spread.append(i)
            visited[i] = True
            count+=1

print(count)