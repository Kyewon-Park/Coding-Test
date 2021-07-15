n, m = map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))

def find_parent(parents,x):
    if parents[x]!=x:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union(parents,a,b):
    a = find_parent(parents,a)
    b = find_parent(parents,b)
    if a>b:
        parents[a]=b
    else:
        parents[b]=a

parents=[0]*(n+1)
for i in range(1,n+1):
    parents[i]=i

for i in range(n):
    for j in range(n):
        if(i>j):
            continue
        if graph[i][j] == 1:
            union(parents, i+1, j+1)

now=plan[0]
for p in plan[1:]:
    if find_parent(parents, now)!=find_parent(parents, p):
        print("NO")
        break
    else:
        if(p==plan[-1]):
            print("YES")
            break
        now=p

# 5 4
# 0 1 0 1 1
# 1 0 0 1 0
# 0 0 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
#=>NO