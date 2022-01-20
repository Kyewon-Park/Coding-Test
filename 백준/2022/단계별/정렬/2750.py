#수 정렬하기

import sys
input = sys.stdin.readline
n=int(input())
l = []
for _ in range(n):
    i = int(input())
    l.append(i)
l.sort()
for i in l:
    print(i)