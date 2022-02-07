#회의실 배정
import sys
input = sys.stdin.readline
n = int(input().strip())
l=[]
for _ in range(n):
    l.append(tuple(map(int,input().strip().split())))
l.sort(key=lambda x: (x[1], x[0]))
print(l)
end = 0
ans = 0
for s, e in l:
    if s>=end:
        ans+=1
        end = e
print(ans)

