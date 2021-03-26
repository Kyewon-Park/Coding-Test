from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range (n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph[0][0] = 2
def bfs(x,y):
    queue = deque([(x,y)])
    while(queue):
        print(graph)
        a,b = queue.popleft()
        if(graph[a][b]>=1):
            for i in range(4):
                nx = a + dx[i] #new x, y for each
                ny = b + dy[i]
                if(nx<0 or nx>=n or ny>=m or ny<0 or graph[nx][ny]!=1):
                    continue
                queue.append((nx,ny))
                if(graph[nx][ny]==1):
                    graph[nx][ny]=graph[a][b]+1
    return graph[n-1][m-1] - 1
print(bfs(0,0))