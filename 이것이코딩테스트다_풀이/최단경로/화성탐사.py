#n=5
#graph=[[3,7,2,0,1],[2,8,0,9,1],[1,2,1,8,1],[9,8,9,2,0],[3,6,5,1,5]]
n=3
graph= [[5,5,4],[3,9,1],[3,2,7]]
for i in range(n):
    for j in range(n):
        if(i==0):
            up=0
        else:
            up=graph[i-1][j]
        if(j==0):
            left=0
        else:
            left=graph[i][j-1]

        if(up==0):
            graph[i][j]=left+graph[i][j]
        elif(left==0):
            graph[i][j]=up+graph[i][j]
        else:
            graph[i][j]=min(left,up)+graph[i][j]

print(graph)