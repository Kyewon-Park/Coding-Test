#여행경로

from collections import deque
def solution(tickets):
    answer=[]
    tl = len(tickets)
    for i in range(tl):
        visited=[False]*tl
        visited[i]=True
        path=[tickets[i][0]]
        answer.append(dfs(tickets[i], visited, tickets, path)) #리스트 리턴
    return answer

def dfs(previous, visited, tickets, path):
    paths=[]
    for i in range(len(tickets)):
        if(not visited[i] and tickets[i][0] == previous[1]):
            visited[i]=True
            path.append(tickets[i][0])
            path = dfs(tickets[i], visited, tickets, path)
        paths.append(path)
    return paths


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))









    # for i in range(tl):
    #     queue=deque([tickets[i]])
    #     while(queue):
    #         start, through = queue.popleft()
    #         answer.append(start)
    #         for i in range(tl):
    #             if(not visited[i] and tickets[i][0] == through):
    #                 queue.append(tickets[i])