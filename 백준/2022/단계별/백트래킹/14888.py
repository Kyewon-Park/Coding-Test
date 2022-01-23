#연산자 끼워넣기
import itertools
n=int(input())
nl = list(input().split())
a,b,c,d = map(int,input().split())
eql = []
for _ in range(a):
    eql.append('+')
for _ in range(b):
    eql.append('-')
for _ in range(c):
    eql.append('*')
for _ in range(d):
    eql.append('//')
eqs = set(itertools.permutations(eql,n-1))
max=0
min=1000000000
for e in eqs:
    val = nl[0]
    for i in range(n-1):
        if e[i]=='//' and int(val)<0:
            val = str(abs(int(val))//int(nl[i+1])*(-1))
        else:
            val = str(eval(val+e[i]+nl[i+1]))
    val=int(val)
    if max<val:
        max=val
    if min>val:
        min=val
print(max)
print(min)
