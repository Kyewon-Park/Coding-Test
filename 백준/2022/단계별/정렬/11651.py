#좌표 정렬하기2
import sys
input=sys.stdin.readline
n=int(input().strip())
l=[]
for _ in range(n):
    a, b = map(int, input().strip().split())
    l.append((a,b))
l.sort(key=lambda x:(x[1], x[0]))
for i in l:
    print(f"{i[0]} {i[1]}")