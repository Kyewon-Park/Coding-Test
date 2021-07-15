#위상정렬
from collections import deque

n=int(input())
graph=[[] for _ in range(n+1)]
indegrees=[]
for i in range(1,n+1):
    cl = list(map(int,input().split()))
    pre=[]
    for j in cl[1:]:
        while(j!= -1):
            pre.append(j)
    graph[i].append((cl[0],pre))
    indegrees[i]=len(pre)

q=deque()
for i in indegrees[1:]:
    if i==0:
        q.append(i)

while(q):
    #뽑음
    now = q.popleft()
    

    #새로넣음
    for i in graph[now][1]:
        indegrees[i]-=1
        if indegrees[i]==0:
            q.append(i)
    
