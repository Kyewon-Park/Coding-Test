#부녀회장이 될테야 

t=int(input())
d = [[0]*15 for _ in range(15)]
for i in range(1,15):
    d[0][i]=i
for i in range(0,15):
    d[i][1]=1
for i in range(1,15):
    for j in range(1,15):
        d[i][j]=d[i-1][j]+d[i][j-1]

for _ in range(t):
    k=int(input())
    n=int(input())
    print(d[k][n])