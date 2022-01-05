#OX퀴즈

from sys import stdin
input=stdin.readline

d = [0]*81
for i in range(81):
    d[i]=i+d[i-1]

n=int(input())
for _ in range(n):
    a=0
    l = list(input().strip().split("X"))
    for i in l:
        a += d[len(i)]
    print(a)