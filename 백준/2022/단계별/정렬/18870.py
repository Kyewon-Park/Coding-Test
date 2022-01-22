#좌표 압축
import sys
n=int(sys.stdin.readline().strip())
l = list(map(int,sys.stdin.readline().strip().split()))
s = set(l)
sl = sorted(list(s))
ans=[]
for i in l:
    ans.append(sl.index(i))
print(*ans, sep=' ')