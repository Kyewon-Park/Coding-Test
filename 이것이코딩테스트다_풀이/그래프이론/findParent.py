#서로소 집합 자료구조는 서로소 부분집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조이다.
#서로소집합 = 공통원소가 없는 두 집합.

#union연산 = 2개의 집합을 하나의 집합으로 합치는 연산.
#find연산 = 특정 원소가 속한 집합이 어떤 집합인지 

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e = map(int,input().split())
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i]=i


cycle=False
for i in range(e):
    a, b = map(int,input().split())
    if find_parent(a) == find_parent(b):
        cycle=True    
        print("싸이클 발생")
        break
    else:
        union_parent(parent, a ,b)
        print("싸이클 발생하지 않음")





