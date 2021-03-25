#가까운 노드부터 탐색.
#선입선출 큐 자료구조 이용함.

#1. 탐색시작 노드를 큐에 넣고 방문처리
#2. 큐에서 노드를 꺼내어 해당 노드의 인접 노드들 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리함.

#보통의 경우 BFS가 DFS보다 빨리 동작함.
#deque라이브러리를 사용하는 것이 좋으며 탐색에 O(N) 소요됨.

from collections import deque #double ended queue

def bfs(graph, start, visited):
    #디큐 생성
    queue = deque([start])
    #방문처리
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False]*len(graph)
bfs(graph,1,visited)


#탐색문제를 보면 그래프 형태로 표현한 다음 문제를 풀어보도록 하자.