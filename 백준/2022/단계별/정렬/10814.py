#나이순 정렬
import sys
input=sys.stdin.readline
n=int(input().strip())
l=[]
for _ in range(n):
    age, name = input().strip().split()
    l.append((int(age),name))
l.sort(key=lambda x:x[0])
for i in l:
    print(f"{i[0]} {i[1]}")
