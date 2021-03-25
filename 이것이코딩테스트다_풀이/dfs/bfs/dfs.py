#스택 자료구조를 활용하는 알고리즘 => 재귀함수를 이용하여 간편하게 구현할 수 있다.

# def factorial(n):
#     if(n<=1):
#         return 1
#     return n * factorial(n-1)

# factorial(5)

#그래프는 노드, 간선으로 표현되며
#프로그래밍에서 그래프는 2가지 방식으로 표현할 수 있다. => 인접행렬, 인접리스트

#인접 행렬 방식은 2차원 배열에 각 노드 연결 형태를 기록하는 방식이다. 
#연결되어 있지 않은 노드들끼리는 INF비용이라고 작성한다. ex) INF=999999999
#graph = [ [0,7,5],
#          [7,0,INF],
#          [5,INF,0] ]

#인접 리스트 방식에서는 모든 노드에, 연결된 노드에 대한 정보를 차례대로 연결하여 저장한다.
# graph = [[] for _ in range(3)] # 노드 3개
# graph[0].append((1,7)) #(노드, 거리)
# ...

#인접행렬방식은 메모리 소모가 크지만, 특정 노드를 찾을때 빠르다. 인접리스트방식은 순회한다.

#dfs과정
# 탐색 시작 노드를 스택에 삽입하고, 방문처리
# 스택의 최상단 노드에 방문하지 않는 노드가 있으면 방문처리하고 스택에 넣는다. 
# 방문처리를 할 노드가 없다면 스택 최상단에서 해당 노드 제거

#dfs 메서드 정의: 간 곳을 순서대로 프린트함
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=" ")
    for node in graph[v]:
        if not visited[node]:
            dfs(graph , node , visited)

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False]*len(graph)
dfs(graph,1,visited)