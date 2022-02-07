#전깃줄
import sys
input = sys.stdin.readline
n = int(input().strip())
l=[]
for _ in range(n):
    l.append(list(map(int,input().strip().split())))
print(l)
cross=[0]*n
delcount=0
while(True):
    for i in range(n):
        for j in range(n):
            if (l[i][0]>l[j][0] and l[i][1]<l[j][1]) or (l[i][0]<l[j][0] and l[i][1]>l[j][1]):
                cross[i]+=1
    idx = cross.index(max(cross))
    l[idx][0]=l[idx][1]=0
    delcount+=1
    if max(cross)==0:
        break
print(delcount)