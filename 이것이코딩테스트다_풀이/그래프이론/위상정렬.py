#순서를 나열할 "방향 그래프"에 적용

#여러가지 조건의 흐름들을 일렬로 나열할 수 있게
#여러개의 답이 존재할 수 있음.
#단방향 사이클이 없는 그래프에만 정렬 수행 가능.
#시작점이 존재해야 함.

#1. 스택
#2. 큐(더 많이 사용)

#진입차수 : 먼저 수행되어야 하는 차수


# 진입차수 0인 정점 큐에 삽입
# 큐에서 원소 꺼내 연결된 모든 간선 제거
# 제거하면 다른 정점들 중에서 진입차수가 새롭게 0으로 바뀐 정점이 있을 것임.
# 진입차수가 0인 정점을 큐에 삽입.
# 큐가 빌때까지 반복.
 
from collections import deque

v, e = map(int, input().split())
 #진입차수 0으로 초기화
indegree = [0]*(v+1)
# 간선정보와 진입차수 입력받음
graph = [[] for i in range(v+1)]
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque() # 
    #맨 처음 진입차수 0인 노드를 큐에 삽입.(시작점)
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    # 큐가 빌 때까지 반복하는 일
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if(indegree[i]==0):
                q.append(i)

    for i in result:
        print(i, end="")

topology_sort()
