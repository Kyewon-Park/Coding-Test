#정수삼각형
import sys
input = sys.stdin.readline
n = int(input().strip())
l = [list(map(int,input().strip().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i+1):
        if j==0:
            l[i][j] = l[i-1][j] + l[i][j]
        elif j==i:
            l[i][j] = l[i-1][j-1] + l[i][j]
        else:
            l[i][j] = max(l[i-1][j],l[i-1][j-1])+l[i][j]
print(max(l[n-1]))