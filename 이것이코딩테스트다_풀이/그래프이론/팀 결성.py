def find_parents(parents, x):
    if parents[x]!=x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b

n, m = map(int, input().split())
parents=[0]*(n+1)
for i in range(n+1):
    parents[i]=i

for i in range(m):
    do, a, b = map(int,input().split())
    if do==1: #1 a b 팀 같은지 여부 확인
        a = find_parents(parents,a)
        b = find_parents(parents,b)
        if(a==b):
            print("YES")
        else:
            print("NO")
    else: #0 a b 팀 합침
        union(parents,a,b)

