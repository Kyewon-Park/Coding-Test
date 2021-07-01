import itertools
import copy

def findNum(graph, targetNum):
    zeros=[]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if(graph[i][j]==targetNum):
                zeros.append((i,j))
    return zeros

def countNum(graph, targetNum):
    count=0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if(graph[i][j]==targetNum):
                count+=1
    return count

def dfs(graph,x,y):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    n = len(graph)
    m = len(graph[0])
    if(graph[x][y]==2):
        for d in range(4):
            if(x+dx[d]>=0 and x+dx[d]<m and y+dy[d]<n and y+dy[d]>=0 and graph[x+dx[d]][y+dy[d]]==0):
                graph[x+dx[d]][y+dy[d]]=2
                graph = dfs(graph,x+dx[d],y+dy[d])
    return graph   

def solution():
    n, m = map(int,input().split())
    graph=[]
    counts=0 #안전영역 크기 배열
    for _ in range(n):
        graph.append(list(map(int,input().split())))

    #find zeros
    zeros = findNum(graph, 0)
    #pick 3
    z3 = list(itertools.combinations(zeros,3))
    
    #simulate
    for z in z3:
#        tempGraph = graph[:]
        tempGraph = copy.deepcopy(graph)
        #맵 바꿈 (1 추가)
        for p in z:
            tempGraph[p[0]][p[1]] = 1

        #dfs (2 퍼짐)
        for i in range(n):
            for j in range(m):
                tempGraph = dfs(tempGraph,0,0) 

        counted = countNum(tempGraph,0)        
        if counts < counted:
            counts = counted
            showGraph(tempGraph)

    return counts

def showGraph(graph):
    n = len(graph)
    #m = len(graph[0])
    for i in range(n):
        print(graph[i])
            

print(solution())