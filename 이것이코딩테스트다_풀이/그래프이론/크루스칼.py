
def find_parents(parent,x):
    if parent[x]!=x:
        parent[x] = find_parents(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parents(parent,a)
    b = find_parents(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n=7 
e=9
input = [(1,2,29),(1,5,75),(2,3,35),(2,6,34),(3,4,7),(4,6,23),(4,7,13),(5,6,53),(6,7,25)]
parent = [0]*(n+1)
edges=[]
result=0

for i in range(1,n+1):
    parent[i]=i

for i in input:
    a,b,cost = i
    edges.append((cost,a,b)) #비용 순 정렬 위해 첫번째 원소 기준으로 비용 설정

edges.sort()
print(edges)
for edge in edges:
    cost,a,b = edge
    if(find_parents(parent,a) != find_parents(parent,b)):
        union_parent(parent,a,b)
        result+=cost

print(result)