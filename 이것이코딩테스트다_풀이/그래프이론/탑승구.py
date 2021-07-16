g = int(input())
p = int(input())
parents=[0]*(g+1)
def find_parents(parents, x):
    if parents[x]!=x:
        parents[x]=find_parents(parents, parents[x])
    return parents[x]
for i in range(1,g+1):
    parents[i]=i



