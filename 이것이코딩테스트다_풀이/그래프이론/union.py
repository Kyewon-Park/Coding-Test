def get_parents(parent, x):
    #루트노드는 parent[x]==x이다.
    if(parent[x]!=x):
        parent[x] = get_parents(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    pa = get_parents(parent, a)
    pb = get_parents(parent, b)
    if pa<pb:
        parent[b]=pa
    else:
        parent[a]=pb

unions = [(6,4),(1,4),(2,3),(2,4),(5,6)]
#노드간선 개수 입력받기
v,e = 6,5
#부모노드 초기화
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

#union연산 수행
for u in unions:
    #재귀적으로 부모노드 찾기
    union(parent,u[0],u[1])

print(parent)
