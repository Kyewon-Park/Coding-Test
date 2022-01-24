#덩치
#!!!!!!!
import sys
input = sys.stdin.readline
n=int(input())
l = []
for _ in range(n):
    a,b = map(int,input().split())
    l.append((a,b))
ans=[]
for i in range(n):
    count=1
    for j in range(n):
        if i==j:
            continue
        if l[i][0]<l[j][0] and l[i][1]<l[j][1]:
            count+=1
    ans.append(count)
print(*ans)