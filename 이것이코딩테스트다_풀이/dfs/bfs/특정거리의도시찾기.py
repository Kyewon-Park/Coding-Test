from collections import deque

def solution(n,m,k,x,graph):
    distance = [-1]*(n+1)
    distance[x]=0

    queue = deque([x])
    while(queue):
        start = queue.popleft()
        for next_node in graph[start]:
            if(distance[next_node]==-1):
                distance[next_node]=distance[start]+1
                queue.append(next_node)
    
    answer=[]
    for i in range(1,n+1):
        if distance[i]==k:
            answer.append(i)

    return answer


print(solution(4,4,2,1,[[],[2,3],[3,4],[],[]]))