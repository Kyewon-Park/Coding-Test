#미로 탐색 bfs
from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[] 
for i in range(n):
    graph.append(list(map(int,list(input())[:-1])))
x=0
y=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
queue=deque([(0,0)])
while queue:
    a,b = queue.popleft()
    if a==n-1 and b==m-1: #마지막
        print(graph[a][b])        
        break
    for i in range(4): #dx,dy 적용
        cx = dx[i]+b
        cy = dy[i]+a
        if cx<0 or cx>=m or cy<0 or cy>=n:
            continue
        if graph[cy][cx]==1:
            graph[cy][cx]+=graph[a][b]
            queue.append((cy,cx))