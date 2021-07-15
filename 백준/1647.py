def find_parent(parents,x):
    if parents[x]!=x:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a>b:
        parents[a]=b
    else:
        parents[b]=a

n, m = map(int, input().split())
edges=[]
parents=[0]*(n+1)
for i in range(n+1):
    parents[i]=i

for i in range(m):
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))
edges.sort()

result=0
biggest=0
for cost, a, b in edges:
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents,a,b)
        result += cost
        biggest = cost

print(result-biggest)