#단어정렬
import sys
input = sys.stdin.readline
n=int(input())
s = set()
for i in range(n):
    s.add(input().strip())
l = sorted(list(s))
l = sorted(l,key=lambda x:len(x))
for i in l:
    print(i)
