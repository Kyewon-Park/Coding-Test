import sys
input=sys.stdin.readline
n=int(input())
tri=[]
for _ in range(n):
    tri.append(list(map(int,input().split())))
for i in range(n-1,0,-1): 
    for j in range(i): 
        tri[i-1][j]= max(tri[i-1][j]+tri[i][j], tri[i-1][j]+tri[i][j+1])
print(tri[0][0])