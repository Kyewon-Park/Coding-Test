#전깃줄
import sys
input = sys.stdin.readline
n = int(input().strip())
l=[]
for _ in range(n):
    l.append(list(map(int,input().strip().split())))
l.sort(key=lambda x:(x[0],x[1]))
count=0
lastl = 0
lastr = 0
for i in l:
    if i[0]>lastl and i[1]>lastr:
        count+=1
        lastl = i[0]
        lastr = i[1]
count = min(count, n-count)
left = n-count
secondcount=0
lastl = 501
lastr = 501
for i in range(n-1,-1,-1):
    if l[i][0]<lastl and l[i][1]<lastr:
        secondcount+=1
        lastl = l[i][0]
        lastr = l[i][1]
secondcount = min(secondcount, left-secondcount)
print(count+secondcount)