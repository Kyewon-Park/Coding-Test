#평균은 넘겠지

from sys import stdin
input=stdin.readline
n= int(input())
for _ in range(n):
    l = list(map(int,input().split()))
    mean = sum(l[1:])/l[0]
    count=0
    for i in l[1:]:
        if i>mean:
            count+=1
    print(f"{count/l[0]*100:.3f}%")